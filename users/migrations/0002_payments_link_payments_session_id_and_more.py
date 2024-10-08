# Generated by Django 4.2.14 on 2024-07-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=400, null=True, verbose_name="ID сессии"
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_amount",
            field=models.PositiveIntegerField(
                help_text="Укажите сумму оплаты", verbose_name="Сумма оплаты"
            ),
        ),
    ]
