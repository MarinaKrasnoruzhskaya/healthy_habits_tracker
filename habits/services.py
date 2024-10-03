from datetime import timedelta

import requests

from config import settings


def send_telegram_message(chat_id, message):
    """ Отправка уведомления в TG """

    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage', params=params)


def get_next_reminder(current_date_reminder, periodicity):
    """ Определение даты следующего напоминания """

    if periodicity == '1 time in 1 days':
        return current_date_reminder + timedelta(days=1)
    elif periodicity == '1 time in 2 days':
        return current_date_reminder + timedelta(days=2)
    elif periodicity == '1 time in 3 days':
        return current_date_reminder + timedelta(days=3)
    elif periodicity == '1 time in 4 days':
        return current_date_reminder + timedelta(days=4)
    elif periodicity == '1 time in 5 days':
        return current_date_reminder + timedelta(days=5)
    elif periodicity == '1 time in 6 days':
        return current_date_reminder + timedelta(days=6)
    elif periodicity == '1 time in 7 days':
        return current_date_reminder + timedelta(days=7)
