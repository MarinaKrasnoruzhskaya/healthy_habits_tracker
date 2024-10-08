# Generated by Django 5.1.1 on 2024-10-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_habit_next_reminder_alter_habit_periodicity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.CharField(
                choices=[
                    ("1 time in 5 days", "1 раз в 5 дня"),
                    ("1 time in 2 days", "1 раз в 2 дня"),
                    ("1 time in 3 days", "1 раз в 3 дня"),
                    ("1 time in 1 days", "1 раз в день"),
                    ("1 time in 6 days", "1 раз в 6 дня"),
                    ("1 time in 4 days", "1 раз в 4 дня"),
                    ("1 time in 7 days", "1 раз в неделю"),
                ],
                default="1 time in 1 days",
                help_text="Укажите периодичность выполнения привычки",
                max_length=30,
                verbose_name="Периодичность выполнения",
            ),
        ),
    ]
