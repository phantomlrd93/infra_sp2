# Проект YaMDb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
# Техническое описание проекта YaMDb
Вам доступен репозиторий api_yamdb, в нём сохранён пустой Django-проект.
К проекту по адресу http://127.0.0.1:8000/redoc/ подключена документация API YaMDb. В ней описаны возможные запросы к API и структура ожидаемых ответов. Для каждого запроса указаны уровни прав доступа: пользовательские роли, которым разрешён запрос.
### Как запустить проект:

Запустить проект:

Перейти в папку infra и запустить docker-compose.yaml
(при установленном и запущенном Docker)
```
cd infra_sp2/infra
docker-compose up
```

Для пересборки контейнеров выполнять команду:
(находясь в папке infra, при запущенном Docker)
```
docker-compose up -d --build
```

В контейнере web выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Проверьте работоспособность приложения, для этого перейдите на страницу:

```
 http://localhost/admin/
```

***Документация*** (запросы для работа с API):

```
 http://localhost/redoc/
```

# Примеры запросов

Регистрация нового пользователя:

```
curl -X POST http://127.0.0.1:8000/api/v1/auth/signup/
   -H 'Content-Type: application/json'
   -d '{"email": "string","username": "string"}'
```
Получение JWT-токена

```
curl -X POST http://127.0.0.1:8000/api/v1/auth/token/
   -H 'Content-Type: application/json'
   -d '{"username": "string", "confirmation_code":"string"}'
```

# Авторы
Александр Петров,
Сергей Ларин,
Алексей Андреев.