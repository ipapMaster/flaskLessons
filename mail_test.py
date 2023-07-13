# mail_test.py
# pip install python-dotenv
from mail_sender import send_mail
from dotenv import load_dotenv

send_mail('mail', 'Вам письмо', 'Текст письма')
