import requests
import allure
from config import BASE_URL, TEST_DATA
from selenium import webdriver

class Test_API:

    def __init__(self, driver: webdriver) -> None:
        self.__driver = driver

    @allure.step("Поиск фильма по ID")
    def testsearchfilmbyid(self):
        response = requests.get(f"{BASE_URL}/api/films/{TEST_DATA:'film''id'}")
        assert response.statuscode == 200
        assert 'name' in response.json()

    @allure.step("Поиск фильма по названию")
    def testsearchfilmbyname(self):
        response = requests.get(f"{BASE_URL}/api/films", params={"name": TEST_DATA['film']['name']})
        assert response.statuscode == 200
        assert len(response.json()) > 0

    @allure.step("Поиск по фильтрам")
    def testsearchbyfilters(self):
        response = requests.get(f"{BASE_URL}/api/films", params=TEST_DATA['film']['filters'])
        assert response.statuscode == 200
        assert len(response.json()) > 0

    @allure.step("Поиск актера по ID")
    def testsearchactorbyid(self):
        response = requests.get(f"{BASE_URL}/api/actors/{TEST_DATA :'film''id'}")
        assert response.statuscode == 200
        assert 'name' in response.json()

    @allure.step("Некорректный поиск по фильтрам")
    def testinvalidfiltersearch(self):
        response = requests.get(f"{BASE_URL}/api/films", params={"genre": "неизвестный жанр"})
        assert response.statuscode == 404