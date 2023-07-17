from requests import get, post

# тестируем наш API (get-запросы)
print(get('http://127.0.0.1:5000/api/news/3').json())
print(get('http://127.0.0.1:5000/api/news/33').json())
print(get('http://127.0.0.1:5000/api/news/q').json())

# post - запросы
# пустой запрос
print(post('http://127.0.0.1:5000/api/news', json='').json())
# неполный запрос
print(post('http://127.0.0.1:5000/api/news',
           json={'title': 'Заголовок'}).json())
# корректный запрос
print(post('http://127.0.0.1:5000/api/news',
           json={'title': 'Заголовок API',
                 'content': 'Новость API',
                 'user_id': 1,
                 'is_private': False
                 }).json())
