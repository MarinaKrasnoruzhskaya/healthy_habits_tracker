from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message, get_next_reminder


@shared_task
def sending_notifications():
    """ Рассылка уведомлений-напоминания о том, в какое время какие привычки необходимо выполнять """

    current_date = datetime.now().date()
    current_time = datetime.now().time()

    habit_list = Habit.objects.filter(next_reminder=current_date, time__lte=current_time)

    for habit in habit_list:
        if habit.user.tg_chat_id:
            send_telegram_message(habit.user.tg_chat_id, habit)
        habit.next_reminder = get_next_reminder(habit.next_reminder, habit.periodicity)
        habit.save()
