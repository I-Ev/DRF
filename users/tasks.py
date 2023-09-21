from datetime import datetime, timedelta

from users.models import User


def check_active_clients():
    """Проверяет активных пользователей за последние 30 дней."""
    cutt_off_date = datetime.now() - timedelta(days=30)
    not_active_clients = User.objects.filter(
        last_login__lt=cutt_off_date
    )
    for client in not_active_clients:
        client.is_active = False
        client.save()