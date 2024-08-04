from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from users.models import User


@shared_task
def check_last_login():

    now = timezone.now()
    month_ago = now - relativedelta(months=1)
    users = User.objects.filter(is_active=True, last_login__lte=month_ago)
    users.update(is_active=False)
