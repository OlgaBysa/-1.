import requests
# import allure

     #Поиск фильма по ID:

# @allure.feature('Поиск фильма')
# @allure.story('Поиск фильма по ID')
def test_search_movie_by_id():
    movie_id = '75209b22'
    response = requests.get(f'https://api.kinopoisk.ru/v1.3/movie/{movie_id}')
    if response.status_code == 404:
        print("Фильм с таким ID не найден")
    else:
     assert response.status_code == 200
     assert response.json()['id'] == movie_id
    
     #Поиск фильма по названию:
def test_search_movie_by_title():
    title = 'Интерстеллар'
    response = requests.get(f'https://api.kinopoisk.ru/v1.3/movie/search', params={'query': title})
    if response.status_code == 404:
        print("Фильм с таким названием не найден")
    else:
        assert response.status_code == 200
        assert any(movie['title'] == title for movie in response.json()['movies'])

     #Поиск по фильтрам:
def test_search_movie_by_filters():
    filters = {'year': 2020, 'genre': 'драма'}
    response = requests.get(f'https://api.kinopoisk.ru/v1.3/movie/search', params=filters)
    if response.status_code == 404:
        print("Фильмы с такими фильтрами не найдены")
    else:
        assert response.status_code == 200
        assert all(movie['year'] == 2020 and 'драма' in movie['genres'] for movie in response.json()['movies'])

     #Поиск актрисы (актера) по ID:
def test_search_actor_by_id():
    actor_id = 'f22e0093'  
    response = requests.get(f'https://api.kinopoisk.ru/v1.3/person/{actor_id}')
    if response.status_code == 404:
        print("Актер с таким ID не найден")
    else:
        assert response.status_code == 200
        assert response.json()['id'] == actor_id
    
     #Некорректный поиск по фильтрам:
def test_invalid_search_by_filters():
    filters = {'year': 'invalid', 'genre': 'unknown'}
    response = requests.get(f'https://api.kinopoisk.ru/v1.3/movie/search', params=filters)
    if response.status_code == 404:
        print("Фильмы с такими фильтрами не найдены")
    else:
        assert response.status_code == 400 