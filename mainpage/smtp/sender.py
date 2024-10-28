from django.core.mail import get_connection
from django.core.mail import send_mail
from django.conf import settings


def smtp():
    connection = get_connection(
        host="smtp.gmail.com",
        port=587,
        username="ExtroEdLive@gmail.com",
        password="bvzl ayje wxxp yjxc",
        use_tls=True,
    )
    return connection


def send_test_email():
    try:
        send_mail(
            'Тема письма',
            'Текст вашего письма здесь.',
            settings.EMAIL_HOST_USER,
            ['ExtroEdLive@gmail.com'],
            fail_silently=False,  # Не подавлять ошибки
        )
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
