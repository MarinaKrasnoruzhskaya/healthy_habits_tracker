# Трекер полезных привычек

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек.
Хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:
я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка
не должна расходовать на выполнение больше двух минут.

## Инструкции по установке

1. Клонировать репозиторий
   ```sh
   git clone git@github.com:MarinaKrasnoruzhskaya/healthy_habits_tracker.git
   ```
2. Перейти в директорию
   ```sh
   cd healthy_habits_tracker
   ```
3. Установить виртуальное окружение
   ```sh
   python -m venv env
   ```
4. Активировать виртуальное окружение
   ```sh
   env\Scripts\activate
   ```
5. Установить зависимости
   ```sh
   pip install -r requirements.txt
   ```
6. Заполнить файл ```.env.sample``` и переименовать его, дав имя ```.env```
7. Создать БД ```healthy_habits_tracker```
   ```
   psql -U postgres
   create database healthy_habits_tracker;  
   \q
   ```
8. Применить миграции
    ```sh
   python manage.py migrate
    ```
9. Заполнить БД
    ```sh
   python manage.py fill
   ```
10. Запустить Celery worker
   ```sh
   celery -A config worker -l INFO
   ```
11. Запустить планировщик Celery beat
   ```sh
   celery -A config beat -l info -S django
   ```    

## Руководство по использованию

1. Для запуска проекта в терминале IDE выполните команду:

  ```sh
   python manage.py runserver
   ```

## Пользователи проекта:

1. Superuser: {"email": "", "password": "admin"}
2. Users: {"email": ", "password": "123456"}, 

## Построен с:

1. Python 3.12
2. env
3. Django 5.0.6
4. Python-dotenv 1.0.1
5. Psycopg2-bynary 2.9.9
6. djangorestframework 3.15.2

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
<p align="right">(<a href="#readme-top">Наверх</a>)</p>

