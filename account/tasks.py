from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_activation_code(email, activation_code):
    activation_link = f'http://34.170.17.83/account/activate/{activation_code}'
    message = f'Активируйте аккаунт, перейдя по ссылке\n{activation_link}'
    send_mail('Activate account', message, 'aanastasiyatuz@gmail.com', [email])
    return "Отправленно"


