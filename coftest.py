import pytest
import requests
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import BASE_URL, TEST_DATA



@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicity_wait(4)
    browser.maximize_window()
    yield browser

    browser.quit()