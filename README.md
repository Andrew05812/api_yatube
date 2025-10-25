# API Yatube

## Описание

API для социальной сети Yatube. Позволяет пользователям публиковать посты, комментировать их, подписываться на авторов и объединять посты в группы.

## Технологии

- Python 3.9
- Django 3.2
- Django REST Framework 3.12
- JWT-токены для аутентификации

## Установка

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Выполните миграции:
```bash
cd yatube_api
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер:
```bash
python manage.py runserver
```

## Примеры запросов

### Получение JWT-токена
```
POST /api/v1/jwt/create/
{
  "username": "your_username",
  "password": "your_password"
}
```

### Получение списка постов
```
GET /api/v1/posts/
```

### Создание поста
```
POST /api/v1/posts/
Headers: Authorization: Bearer <your_token>
{
  "text": "Текст поста",
  "group": 1
}
```

### Подписка на пользователя
```
POST /api/v1/follow/
Headers: Authorization: Bearer <your_token>
{
  "following": "username"
}
```

### Получение списка подписок
```
GET /api/v1/follow/
Headers: Authorization: Bearer <your_token>
```

## Документация

Полная документация API доступна по локальному адресу: http://127.0.0.1:8000/redoc/

## Автор

@Andrew05812