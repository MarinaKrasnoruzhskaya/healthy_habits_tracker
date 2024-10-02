from datetime import timedelta, datetime

from django.db import models

from config.settings import AUTH_USER_MODEL


NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """ Класс для модели Привычка """

    PERIODS = {
        ("1 time in 1 days", "1 раз в день"),
        ("1 time in 2 days", "1 раз в 2 дня"),
        ("1 time in 3 days", "1 раз в 3 дня"),
        ("1 time in 4 days", "1 раз в 4 дня"),
        ("1 time in 5 days", "1 раз в 5 дня"),
        ("1 time in 6 days", "1 раз в 6 дня"),
        ("1 time in 7 days", "1 раз в неделю"),
    }

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        **NULLABLE
    )
    place = models.CharField(
        max_length=60,
        verbose_name="Место выполнения",
        help_text="Укажите место выполнения привычки",
    )
    time = models.TimeField(
        verbose_name="Время выполнения",
        help_text="Укажите время выполнения привычки",
    )
    action = models.CharField(
        max_length=100,
        verbose_name="Действие",
        help_text="Укажите действие, которое нужно выполнять",
    )
    is_pleasant_habit = models.BooleanField(
        verbose_name="Приятная привычка",
        help_text="Укажите, является ли привычка приятной",
        default=False,
        **NULLABLE,
    )
    associated_habit = models.ForeignKey(
        "Habit",
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="habits",
    )
    periodicity = models.CharField(
        choices=PERIODS,
        default="1 time in 1 days",
        max_length=30,
        verbose_name="Периодичность выполнения",
        help_text="Укажите периодичность выполнения привычки",
    )
    reward = models.CharField(
        max_length=100,
        verbose_name="Вознаграждение",
        help_text="Укажите вознвграждение за выполнение привычки",
        **NULLABLE,
    )
    time_to_complete = models.PositiveIntegerField(
        verbose_name="Время на выполнение",
        help_text="Укажите время на выполнение привычки",
    )
    is_publicity = models.BooleanField(
        verbose_name="Публичная привычка",
        help_text="Укажите, является ли привычка публичная",
        default=False,
        **NULLABLE,
    )

    next_reminder = models.DateField(
        verbose_name="Дата следующего напоминания",
        help_text="Укажите дату следующего напоминания",
        **NULLABLE,
    )

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def save(self, *args, **kwargs):
        """ Определяет дату следующего напоминания: сегодня, если текущее время не превышает задаваемое время
        выполнения привычки, иначе следующий день """

        now_date = datetime.now().date()
        now_time = datetime.now().time()

        if now_time > self.time:
            self.next_reminder = now_date + timedelta(days=1)
        else:
            self.next_reminder = now_date

        super(Habit, self).save(*args, **kwargs)
