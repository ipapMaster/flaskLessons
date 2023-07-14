# loginform.py
# pip install flask-wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms import SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired

# Если из формы добавлен файл,
# то обращаться к нему при обработке формы
# следует так: f.form.<название поля с файлом>.data
# ORM - Object Relationship Mapping

class LoginForm(FlaskForm):
    email = EmailField('Ваша почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
