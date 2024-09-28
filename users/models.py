from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Класс для модели Пользователь"""

    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите email"
    )

    phone = PhoneNumberField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Введите телефон",
        **NULLABLE,
    )
    tg_nick = models.CharField(
        max_length=50,
        verbose_name="Tg name",
        help_text="Введите ник телеграмм",
        **NULLABLE,
    )
    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="Tg chat id",
        help_text="Введите id чата в телеграмме",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
