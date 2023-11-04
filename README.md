# codeunion_tech_task-
test task for codeunion by Aslan Amanzholov.

start command:
1. python3 -m venv venv 
2. source vennv/bin/activate
3. pip install -r requirements.txt # Установка зависимостей
4. docker-compose up db -d # Для запуска и настройки psql
5. python manage.py makemigrations
6. python manage.py migrate # Миграция в базу данных
7. python manage.py crontab add # Для запуска CRON по обновлению валюты
8. python manage.py runserver # Для запуска сервера

# Дополнительные команды
1. python manage.py currency_list
2. python manage.py currency_edit <currency_uuid> <currency_name> <currency_rate>
3. python mannage.py createsuperuser

# Main Endpoints
1. host:port/api/auth/api-token-auth/ # Для авторизации {"email" : "your email", "password": "your password"}