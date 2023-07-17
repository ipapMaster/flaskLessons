import flask
from flask import jsonify, make_response, request

from . import db_session
from .news import News

blueprint = flask.Blueprint('news_api',
                            __name__,
                            template_folder='templates')


@blueprint.route('/api/news')
def get_news():
    # по традиции создаём сессию для работы с БД
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('title', 'content', 'user.name'))
                 for item in news]
        }
    )


@blueprint.route('/api/news/<int:news_id>', methods=['GET'])
def get_one_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        return jsonify({'error': f'Новости по ID-{news_id} не найдены!'})
    return jsonify(
        {
            'news': news.to_dict(only=('title', 'content', 'user_id', 'is_private'))
        }
    )


@blueprint.route('/api/news', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Пустой запрос'})
    elif not all(key in request.json for key in
                 ['title', 'content', 'user_id', 'is_private']):
        print('Вот', request.json)
        return jsonify({'error': 'Некорректный запрос'})
    db_sess = db_session.create_session()
    news = News(
        title=request.json['title'],
        content=request.json['content'],
        user_id=request.json['user_id'],
        is_private=request.json['is_private']
    )
    db_sess.add(news)
    db_sess.commit()
    return jsonify({'success': 'OK'})

@blueprint.route('/api/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    # по традиции создаём сессию для работы с БД
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        return jsonify({'error': 'Nothing to Delete'})
    db_sess.delete(news)
    db_sess.commit()
    return jsonify({'success': 'Deleted'})