import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



   #Проверка доступа на главную страницу:

def test_access_main_page():
    driver = webdriver.Chrome()
    driver.get('https://www.kinopoisk.ru')
    assert 'Кинопоиск' in driver.title

    driver.quit()

    #Проверка поиска фильма по названию:

def test_search_movie_by_title():
    driver = webdriver.Chrome()
    driver.get('https://www.kinopoisk.ru')
    search_box = driver.find_element(By.NAME, 'kp_query')
    search_box.send_keys('Интерстеллар')
    search_box.send_keys(Keys.RETURN)
    assert 'Интерстеллар' in driver.page_source

    driver.quit()

     #Проверка отображения информации о фильме:

def test_display_movie_info():
    driver = webdriver.Chrome()
    driver.get('https://www.kinopoisk.ru')
    search_box = driver.find_element(By.NAME, 'kp_query')
    search_box.send_keys('Интерстеллар')
    search_box.send_keys(Keys.RETURN)
    movie_link = driver.find_element(By.PARTIAL_LINK_TEXT,('Интерстеллар'))
    movie_link.click()

     #Проверка перехода на страницу актера/режиссера:

def test_navigate_to_actor_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.kinopoisk.ru')
    search_box = driver.find_element(By.NAME, 'kp_query')
    search_box.send_keys('Интерстеллар')
    search_box.send_keys(Keys.RETURN)
    
    # Ожидание загрузки ссылки на фильм
    movie_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Интерстеллар'))
    )
    movie_link.click()
    
    # Ожидание загрузки ссылки на актера
    actor_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Мэттью МакКонахи'))
    )
    actor_link.click()
    
    assert 'Мэттью МакКонахи' in driver.page_source
    driver.quit()

    #Проверка фильтрации фильмов по жанрам:

def test_filter_movies_by_genre():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.kinopoisk.ru')
    
    # Ожидание загрузки и клик на меню "Фильмы"
    movies_menu = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Фильмы')]"))
    )
    movies_menu.click()
    
    # Ожидание загрузки и клик на "Жанры"
    genres_menu = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Жанры')]"))
    )
    genres_menu.click()
    
    # Ожидание загрузки и клик на жанр "Драма"
    drama_genre = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Драма')]"))
    )
    drama_genre.click()
    
    # Проверка отображения фильмов жанра "Драма"
    assert 'Драма' in driver.page_source
    driver.quit()
    
    #Проверка добавления фильма в избранное:

def test_add_movie_to_favorites():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.kinopoisk.ru')
    
    # Авторизация
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
    login_button.click()
    
    # Ожидание загрузки поля для ввода email
    email_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys('test@example.com')
    
    # Ожидание загрузки поля для ввода пароля
    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.send_keys('password123')
    
    # Ожидание загрузки кнопки "Войти" и клик на нее
    submit_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Войти')]"))
    )
    submit_button.click()
    
    # Поиск фильма и добавление в избранное
    search_box = driver.find_element(By.NAME, 'kp_query')
    search_box.send_keys('Интерстеллар')
    search_box.send_keys(Keys.RETURN)
    
    # Ожидание загрузки ссылки на фильм
    movie_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Интерстеллар'))
    )
    movie_link.click()
    
    # Ожидание загрузки кнопки "В избранное" и клик на нее
    favorite_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'favorite'))
    )
    favorite_button.click()
    
    # Проверка успешного добавления
    assert 'В избранном' in driver.page_source
    driver.quit()
