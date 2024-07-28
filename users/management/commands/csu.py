from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(email="admin@sky.pro")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        # Метод set_password хеширует открытый пароль
        user.set_password("123")
        user.save()
