# Generated by Django 4.2.14 on 2024-08-04 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_alter_course_options_alter_lesson_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="обновлено"),
        ),
        migrations.AddField(
            model_name="lesson",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="обновлено"),
        ),
    ]
