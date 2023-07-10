# https://github.com/ipapMaster/flaskLessons
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'Адмирал!<br><a href="/slogan">Слоган</a>'

@app.route('/poster')
def poster():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
</head>
<body>
<h1>Постер к фильму</h1>
<img src="{url_for('static', filename='images/admiral.png')}"
alt="Здесь должна был быть картинка, но не нашлась">
<p>И крепка, как смерть, любовь!</p>
</body>
</html>"""


@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть, любовь!<br><a href="/">Назад</a>'


@app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]
    lst.append('Start!!!')
    return '<br>'.join(lst)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
