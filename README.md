# api_final
Yatube API — это REST API для социальной сети Yatube. Сервис позволяет публиковать посты, подписываться на других пользователей, комментировать записи и многое другое.

## Технологии

- Python 3.12
- Django 3.2.16
- Django REST Framework
- SimpleJWT
- Djoser
- Pytest

## Установка и запуск

1. Клонируйте репозиторий:
   ```
   git clone <ссылка_на_репозиторий>
   cd api_final_yatube
   ```

2. Создайте и активируйте виртуальное окружение:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

4. Выполните миграции:
   ```
   python3 yatube_api/manage.py migrate
   ```

5. Запустите сервер:
   ```
   python3 yatube_api/manage.py runserver
   ```

