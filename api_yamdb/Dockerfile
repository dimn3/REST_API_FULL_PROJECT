FROM python:3.7-slim

# Скопировать с локального компьютера файл зависимостей
WORKDIR /app
# в директорию /app.
COPY requirements.txt .

# Выполнить установку зависимостей внутри контейнера.
RUN pip3 install -r /app/requirements.txt --no-cache-dir

# Скопировать содержимое директории /api_yamdb c локального компьютера
# в директорию /app.
COPY . .

# Сделать директорию /app рабочей директорией. 

# Выполнить запуск сервера разработки при старте контейнера.
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]