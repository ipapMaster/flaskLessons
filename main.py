# https://github.com/ipapMaster/flaskLessons
from flask import Flask, url_for, request, redirect
from flask import render_template
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = 'Слушатель'
    param['title'] = 'Расширяем шаблоны'
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf-8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html',
                           title='Новости',
                           news=news_list)
    # lst = ['ANN', 'TOM', 'BOB']
    # return render_template('news.html', title="FOR", news=lst)

@app.route('/vartest')
def vartest():
    return render_template('var_test.html', title='Переменные в HTML')

@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть, любовь!<br><a href="/">Назад</a>'

@app.route('/weather_form', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'GET':
        return render_template('weather_form.html',
                               title='Выбор города')
    elif request.method == 'POST':
        town = request.form.get('town')
        return render_template('weather.html',
                               title=f'Погода в городе {town}',
                               town=town)

@app.route('/form_sample', methods=['GET', 'POST'])
def form_sample():
    if request.method == 'GET':
        return render_template('user_form.html', title='Форма')
    elif request.method == 'POST':
        f = request.files['file']  # request.form.get('file')
        f.save('./static/images/loaded.png')
        myform = request.form.to_dict()
        return render_template('filled_form.html',
                               title='Ваши данные',
                               data=myform)


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return f"""
        <form class="login_form" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="photo">Приложите фото:</label>
                <input type="file" class="from-control-file" id="photo" name="file">
            </div><br>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
        """
    elif request.method == 'POST':
        f = request.files['file']  # request.form.get('file')
        f.save('./static/images/loaded.png')
        return '<h1>Файл у Вас на сервере</h1>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
