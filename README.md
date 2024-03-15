# REST_API_FULL_PROJECT

# адрес работающего сервера 51.250.1.5 (http)
___________________________________________________________________________________________________________________________________________________

Проект представляет собой REST API для проекта, в котором собираются отзывы поьзователей на различные произведения.
В данном проекте REST API для проектаb реализован следующий функционал:
* Получение списка категорий или добавление категории администратором, поиск категории по названию, удаление категорий администратором.
* Получение списка  жанров или добавление жанра администратором, удаление жанра администратором.
* Получение списка произведений или отдельного произведения по id или добавление произведения администратором, удаление произведения администратором,частичное обновление информации по произведению администратором.
* Получение списка отзывов или отдельного отзыва по id, добавление нового отзыва, но только одного на одно произведение Аутентифицированным пользователем, частичное изменение или удаление отзыва автором отзыва, администратором или модератором.
* Получение всех комментариев к отзыву по id.
* Просмотр, создание, удаление и изменение комментариев.
* Создание аккаунта пользователя самим пользователем или суперюзером.
* Авторизация по JWT (JSON Web Token) токену.d
* Регистрация пользователей и управление правами доступа.
  
## Используемые технологии
* requests==2.26.0
* django==2.2.16
* djangorestframework==3.12.4
* gunicorn==20.0.4
* psycopg2-binary==2.8.6
* PyJWT==2.1.0
* pytest==6.2.4
* pytest-django==4.4.0
* pytest-pythonpath==0.7.3
* django-filter==2.4.0
* djangorestframework-simplejwt==4.7.2
