import os

# URL вашего сайта
BASE_URL = "https://kinopoisk.ru"

# Тестовые данные
TEST_DATA = {
    "user": {
        "username": os.getenv("TEST_USERNAME", "your_username"),
        "password": os.getenv("TEST_PASSWORD", "your_password"),
    },
    "film": {
        "id": 4686066, 
        "name": "Поехавшая",
        "filters": {"genre": "комедия", "year": "2023"}, 
    },
}