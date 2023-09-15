from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.ru',
            first_name='useradmin',
            last_name='adminuser',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('0000')
        user.save()
        print('superuser created')