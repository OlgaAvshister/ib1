# Лабораторная работа: Защищённое Backend-приложение на Flask

## Описание проекта

Простой защищённый веб-API на Python + Flask. Цель: практика безопасной разработки и интеграция SAST/SCA инструментов.

---

## API

### 1. POST /auth/login
Аутентификация пользователя. Возвращает JWT-токен.

**Запрос:**
```
POST /auth/login
Content-Type: application/json

{
  "username": "alice",
  "password": "password"
}
```

**Ответ:**
```
{
  "access_token": "<JWT-токен>"
}
```
### 2. GET /api/data
Получение списка постов. Доступ только для аутентифицированных пользователей.

**Запрос:**
```
GET /api/data
Authorization: Bearer <JWT-токен>
```
**Ответ:**
```
[
  {
    "id": 1,
    "author": "alice",
    "title": "Hello",
    "content": "Привет мир"
  }
]
```
### 3. POST /api/data
Создание нового поста

**Запрос:**
```
POST /api/data
Content-Type: application/json
Authorization: Bearer <JWT-токен>

{
  "title": "Мой пост",
  "content": "<b>Контент</b>"
}
```
**Ответ:**
```
{
  "id": 3,
  "msg": "created"
}
```
### Особенности:

HTML-теги экранируются → защита от XSS.

## Меры защиты
1. SQL-инъекции: используется SQLAlchemy ORM, параметризованные запросы.

2. XSS: все пользовательские данные экранируются перед отправкой.

3. Broken Authentication:

  - Пароли хранятся в хешированном виде (bcrypt).

  - JWT-токены используются для защищённых эндпоинтов.

  - Flask debug mode отключен.

## CI/CD (GitHub Actions)
- Workflow находится в .github/workflows/ci.yml.

- Настроен запуск SAST и SCA:

  - Bandit — статический анализ Python-кода.
  - Safety — проверка зависимостей на известные уязвимости.

- Каждое изменение в main автоматически запускает проверки.
