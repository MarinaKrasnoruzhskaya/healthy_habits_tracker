# Generated by Django 5.1.1 on 2024-09-28 08:06

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                help_text="Введите телефон",
                max_length=35,
                null=True,
                region=None,
                verbose_name="Телефон",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                help_text="Введите id чата в телеграмме",
                max_length=50,
                null=True,
                verbose_name="Tg chat id",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="tg_nick",
            field=models.CharField(
                blank=True,
                help_text="Введите ник телеграмм",
                max_length=50,
                null=True,
                verbose_name="Tg name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Введите email",
                max_length=254,
                unique=True,
                verbose_name="Email",
            ),
        ),
    ]
