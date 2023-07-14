from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Содержание')
    is_private = BooleanField('Личная')
    submit = SubmitField('Применить')
