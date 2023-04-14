import requests

from film import Film
from film import Genres


URL_API = "https://kinopoiskapiunofficial.tech/api/v2.2/films/top"
API_KEY = "39fff5b9-9bad-4f10-8453-9473bf112d4e"


# response = requests.get(
#     URL_API,
#     params={"page": 15},
#     headers={
#         "Content_type": "application/json",
#         "X-API-KEY": API_KEY
#     }
# ).json()


# print(response)

# films = []
# for film_hash in response["films"]:
#     film = Film(film_hash)
#     films.append(film)

# for film in films:
#     print(f"{film}\n")

#Получаем все страницы топовых фильмов
def get_all_the_top_movie_pages():
    top_films = []
    top_film_session = requests.Session()
    page = 1

    while True:
        response = top_film_session.get(
                    URL_API,
                    params={"page": page},
                    headers={"Content_type": "application/json","X-API-KEY": API_KEY}
                ).json()
        
        if response["films"] == []:
            break
        
        for film_hash in response["films"]:
            top_films.append(Film(film_hash))
        
        page += 1
    
    top_film_session.close()
    
    return top_films
    


#output_of_all_genres
def we_get_all_genres():
    response = requests.get(
        "https://kinopoiskapiunofficial.tech/api/v2.2/films/filters",
        headers={
            "Content_type": "application/json",
            "X-API-KEY": API_KEY
        }
    ).json()

    all_genres = []
    for genre_hash in response["genres"]:
        all_genres.append(Genres(genre_hash))
        
    for genre in all_genres:
        print(f"{genre}".replace("25.", ""))
    
    return all_genres

we_get_all_genres()

for film in get_all_the_top_movie_pages():
     print(f"{film}\n")