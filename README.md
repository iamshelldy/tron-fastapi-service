# Tron FastAPI Service

## Описание
Приложение позволяет получать и сохранять информацию по адресу в сети Tron о следующих ресурсах:
* баланс
* энергия
* пропускная способность

## Стек
* **Бэкенд**: FastAPI, SQLAlchemy, Alembic, TronPy
* **БД**: PostgreSQL
* **Контейнеризация**: Docker, Docker Compose
* **Тестирование**: Pytest, Swagger UI

## Навигация
* [Предварительные требования](#предварительные-требования)
* [Деплой](#деплой)
  * [Локальная установка](#локальная-установка)
  * [Docker](#docker-деплой)
* [Тестирование](#тестирование)
  * [Pytest](#pytest)
  * [Swagger UI](#swagger-ui)

## Предварительные требования:
* [Ключ TRON API](https://developers.tron.network/reference/select-network#how-to-get-an-api-key)
* Для запуска проекта на локальной машине:
  * [Python 3.11+](https://www.python.org/downloads/)
  * [PostgreSQL (если не используете Docker)](https://www.postgresql.org/download/)
* Для запуска проекта в контейнере:
  * [Docker](https://docs.docker.com/get-docker/)

## Деплой
Клонируйте репозиторий:

```bash
git clone https://github.com/iamshelldy/tron-fastapi-service.git
cd tron-fastapi-service
```

Далее у тебя есть два варианта:
* [Локальная установка](#локальная-установка)
* [Docker](#docker-деплой)

### Локальная установка

Выполните из корня проекта следующие команды:\
Создайте виртуальное окружение:
```bash
python3 -m venv venv  
source venv/bin/activate  # На Windows: venv\Scripts\activate  
```
Установите зависимости Python:
```bash
pip install -r requirements.txt
```
Настройте переменные окружения:\
Создайте файл `.env` по шаблону `.env.template`, укажите параметры подключения к базе данных и ключ TRON API.

Примените миграции базы данных:
```bash
alembic upgrade head
```
Запустите проект:
```bash
uvicorn "app.main:app"
```

### Docker деплой
Настройте переменные окружения:
Создайте файл .env по шаблону .env.template, укажите параметры подключения к базе данных и ключ TRON API.

```bash
DB_HOST=db  # в качестве хоста укажите название контейнера с Postgres. 
```


Соберите и запустите контейнер:
```bash
docker-compose up --build
```

## Тестирование

### Pytest
Запуск тестов, из корня проекта:
```bash
pytest tests/pytest
```

### Swagger UI
Перейдите по адресу http://`host`:`port`/docs\
При настройках по умолчанию: http://localhost:8000/docs
