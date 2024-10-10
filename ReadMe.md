# Трекер полезных привычек

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек.
Хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:
я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка
не должна расходовать на выполнение больше двух минут.
Рассылка напоминаний о необходимости выполнения полезной привычки интегрирована в Телеграмм-бот пользователя. 

## Инструкции по развертыванию проекта с Docker

1. Клонировать репозиторий
   ```sh
   git clone git@github.com:MarinaKrasnoruzhskaya/healthy_habits_tracker.git
   ```
2. Заполнить файл ```.env.sample``` и переименовать его в файл с именем ```.env```
3. Соберите образ и запустите контейнеры
   ```sh
   docker-compose up -d --build
   ```

## Инструкции по развертыванию проекта без Docker

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
6. Заполнить файл ```.env.sample``` и переименовать его в файл с именем ```.env```
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
   python manage.py loaddata data.json
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

1. Superuser: {"email": "admin@hht.com", "password": "admin"}
2. Users: {"email": "user_1@hht.com"", "password": "1234qwer"}, {"email": "user_2@hht.com"", "password": "1234qwer"}, 

## Построен с:

1. Python 3.12
2. env
3. Django 5.0.6
4. Python-dotenv 1.0.1
5. Psycopg2-bynary 2.9.9
6. djangorestframework 3.15.2
7. celery 5.4.0
8. django-celery-beat 2.7.0
9. django-cors-headers 4.4.0
10. djangorestframework-simplejwt 5.3.1
11. drf-spectacular 0.27.2
12. redis 5.1.0
13. requests 2.32.3
14. Docker 27.3.1
15. docker-compose 1.29.2

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
<p align="right">(<a href="#readme-top">Наверх</a>)</p>

