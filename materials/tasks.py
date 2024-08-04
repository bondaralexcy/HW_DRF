import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Course, CourseSubscription
from users.models import User


@shared_task
def send_mail_about_course_update(course_id):
    """Отправка сообщения подписчику об изменении состава курса"""
    course = Course.objects.get(id=course_id)
    course_subs = CourseSubscription.objects.filter(course=course)
    all_email_list = course_subs.values_list("user_email", flat=True)

    for email in all_email_list:
        send_mail(
            subject="Обновление курса",
            message=f"Курс {course.name} был обновлен",
            from_email=EMAIL_HOST_USER,
            recipient_list=all_email_list,
        )
        print(f"Письмо было отправлено по адресу {email}")
