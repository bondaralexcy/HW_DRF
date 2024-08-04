from django.db import models

from config import settings


class Course(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Укажите название курса"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Опишите основные материалы курса",
    )
    preview = models.ImageField(
        upload_to="materials/courses",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Добавьте изображение",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец курса",
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ("title",)


class Lesson(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Укажите название урока"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Опишите содержание урока",
    )
    preview = models.ImageField(
        upload_to="materials/lessons",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Добавьте изображение",
    )
    url = models.URLField(
        verbose_name="Cсылка на видео",
        blank=True,
        null=True,
        help_text="Укажите ссылку на видео",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        blank=True,
        null=True,
        help_text="Укажите курс",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец урока",
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("title",)


class CourseSubscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="подписчик",
        null=True,
        blank=True,
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")

    class Meta:
        verbose_name = "подписка на курс"
        verbose_name_plural = "подписки на курс"

    def __str__(self):
        return f"{self.user} {self.course}"
