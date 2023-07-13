from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль',
                                   validators=[DataRequired()])
    name = StringField('Ваше имя', validators=[DataRequired()])
    about = TextAreaField('Немного о себе')
    submit = SubmitField('Регистрация')
