import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


   #Проверка доступа на главную страницу:

@allure.feature('Главная страница')
@allure.story('Проверка доступа на главную страницу')
def test_access_main_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.kinopoisk.ru')
    assert 'Кинопоиск' in driver.title
    driver.quit()


    #Проверка поиска фильма по названию:

@allure.feature('Поиск фильма')
@allure.story('Поиск фильма по названию')
def test_search_movie_by_title():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.kinopoisk.ru')
    search_box = driver.find_element(By.NAME, 'kp_query')
    search_box.send_keys('Интерстеллар')
    search_box.send_keys(Keys.RETURN)
    assert 'Интерстеллар' in driver.page_source
    driver.quit()
    

     #Проверка отображения информации о фильме:

@allure.feature('Информация о фильме')
@allure.story('Проверка отображения информации о фильме')
def test_display_movie_info():
    driver.get('https://www.kinopoisk.ru')
    driver.maximize_window()
    search_box = driver.find_element(By.NAME, 'kp_query')
    search_box.send_keys('Интерстеллар')
    search_box.send_keys(Keys.RETURN)
    movie_link = driver.find_element(By.PARTIAL_LINK_TEXT,('Интерстеллар'))
    movie_link.click()
    driver.quit()
     #Проверка перехода на страницу актера/режиссера:

@allure.feature('Страница актера')
@allure.story('Проверка перехода на страницу актера/режиссера')
def test_navigate_to_actor_page():
     driver.get('https://www.kinopoisk.ru')
     browser = webdriver.Chrome()
     browser.implicitly_wait(4) 
     browser.maximize_window()
     search_box = driver.find_element(By.NAME, 'kp_query')
     search_box.send_keys('Интерстеллар')
     search_box.send_keys(Keys.RETURN)
    
     # Ожидание загрузки ссылки на фильм
     movie_link = WebDriverWait(driver, 20).until(
         EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Интерстеллар'))
     )
     
     movie_link.click()
    
     # Ожидание загрузки ссылки на актера
    #  WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a[data-tid='d4e8d214']"), " Мэттью МакКонахи"))
     actor_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-tid='d4e8d214' and contains(text(), 'Мэттью МакКонахи')]")))
     actor_link = driver.find_element(By.XPATH, "//a[@data-tid='d4e8d214' and contains(text(), 'Мэттью МакКонахи')]")
    
     actor_link = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a[data-tid='d4e8d214']"), "МакКонахи"))
     actor_link.click()
    
     actor = driver.find_element(By.CSS_SELECTOR, "h1[data-tid='f22e0093']").text
     assert 'Мэттью МакКонахи' in actor
     driver.quit()
     

    
    #Проверка появления окна авторизации:

@allure.feature('Авторизация')
@allure.story('Проверка появления окна авторизации')
def test_authorization_window():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.kinopoisk.ru')
    
    
    # Авторизация
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
    login_button.click()
    driver.quit()
    

 
