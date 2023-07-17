from requests import get, post, delete

# тестируем наш API (get-запросы)
print(get('http://127.0.0.1:5000/api/v2/news/3').json())
print(get('http://127.0.0.1:5000/api/v2/news/33').json())
print(get('http://127.0.0.1:5000/api/v2/news/q').json())

# post - запросы
# пустой запрос
print(post('http://127.0.0.1:5000/api/v2/news', json='').json())
# неполный запрос
print(post('http://127.0.0.1:5000/api/v2/news',
           json={'title': 'Заголовок'}).json())
# корректный запрос
print(post('http://127.0.0.1:5000/api/v2/news',
           json={'title': 'Заголовок API',
                 'content': 'Новость API',
                 'user_id': 1,
                 'is_private': False,
                 'is_published': True
                 }).json())
# print(delete('http://127.0.0.1:5000/api/v2/news/999').json())
# print(delete('http://127.0.0.1:5000/api/v2/news/7').json())