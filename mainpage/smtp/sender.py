from django.core.mail import get_connection


def smtp():
    connection = get_connection(
        host="smtp.gmail.com",
        port=587,
        username="ExtroEdLive@gmail.com",
        password="bvzl ayje wxxp yjxc",
        use_tls=True,
    )
    return connection
