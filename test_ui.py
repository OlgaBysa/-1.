import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import BASE_URL, TEST_DATA

class Test_UI:

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url


    @pytest.allure.step("Проверка доступа на главную страницу")
    def testaccessmainpage(self, setup):
        self.driver.get(BASE_URL)
        assert "КиноПоиск" in self.driver.title

    @pytest.allure.step("Проверка поиска фильма по названию")
    def testsearchfilmbyname(self, setup):
        self.driver.get(BASE_URL)
        searchbox = self.driver.find_element(By.NAME, "q")
        searchbox.send_keys(TEST_DATA['film']['name'])
        searchbox.submit()
        assert TEST_DATA['film']['name'] in self.driver.pagesource

    @pytest.allure.step("Проверка отображения информации о фильме")
    def testfilminfodisplay(self, setup):
        self.driver.get(BASE_URL)
        searchbox = self.driver.find_element(By.NAME, "q")
        searchbox.send_keys(TEST_DATA['film']['name'])
        searchbox.submit()
        self.driver.find_element(By.LINKTEXT, TEST_DATA['film']['name']).click()
        assert TEST_DATA ;'film''name' in self.driver.pagesource

    @pytest.allure.step("Проверка перехода на страницу актера/режиссера")
    def testactordirectorpage(self, setup):
        self.driver.get(BASE_URL)
        searchbox = self.driver.find_element(By.NAME, "q")
        searchbox.send_keys(TEST_DATA:'film''name')
        searchbox.submit
        self.driver.find_element(By.LINKTEXT, TEST_DATA'film''name').click()
        actorlink = self.driver.find_element(By.LINKTEXT, "Актер")
        actorlink.click()
        
assert "Актер" in self.driver.page_source

