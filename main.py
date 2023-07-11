# https://github.com/ipapMaster/flaskLessons
from flask import Flask, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return redirect('/load_photo')  # безусловный редирект


@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть, любовь!<br><a href="/">Назад</a>'


@app.route('/form_sample', methods=['GET', 'POST'])
def form_sample():
    if request.method == 'GET':
        with open('./templates/user_form.html', 'r', encoding='utf-8') as html_stream:
            return html_stream.read()
    elif request.method == 'POST':
        print(request.method)
        print(request.form['fname'])
        print(request.form['sname'])
        return 'Форма отправлена'

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
        f = request.files['file']
        f.save('./static/images/loaded.png')
        return '<h1>Файл у Вас на сервере</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
