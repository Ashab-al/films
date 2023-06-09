import requests

from film import Film


API_KEY = "39fff5b9-9bad-4f10-8453-9473bf112d4e"
URL_API = "https://kinopoiskapiunofficial.tech/api/v2.2/films/top"
URL_API_FILTER = "https://kinopoiskapiunofficial.tech/api/v2.2/films"
URL_API_SEARCH_BY_KEYWORD = "https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword"


# response = requests.get(
#     URL_API,
#     params={"page": 15},
#     headers={
#         "Content_type": "application/json",
#         "X-API-KEY": API_KEY
#     }
# ).json()





# films = []
# for film_hash in response["films"]:
#     film = Film(film_hash)
#     films.append(film)

# for film in films:
#     print(f"{film}\n")




class GenreApiHandler:
        #Проверка существует ли жанр
    def checking_whether_a_genre_exists(selected_genre: int, all_genres: list):
        for genre in all_genres:
            if selected_genre == genre[0]:
                return True

        else:
            return False     

    #api запрос по жанру
    def api_request_by_genre(genre: int, page:int = 1):
        response = requests.get(
                URL_API_FILTER,
                params={"genres": genre, "page": page},
                headers={"Content_type": "application/json", "X-API-KEY": API_KEY}
            ).json()
        return response

    #распаковка api запроса фильмов 
    def unpacking_the_movie_request_api(films_data: dict):
        total_pages: int = films_data["totalPages"]
        total_movies: int = films_data["total"]
        films: list = []

        for film_hash in films_data["items"]:
            films.append(Film(film_hash))
        
        return films
    
    #распаковка api запроса фильмов для функции поиска по названию
    def unpacking_the_movie_request_api_for_search_name(films_data: dict, pagescount: int):
        total_pages = pagescount
        films: list = []

        for film_hash in films_data:
            films.append(Film(film_hash))
        
        return films
    
    #Получить фильмы по ключевым словам
    def get_movies_by_keywords(keywords):
        response = requests.get(
                URL_API_SEARCH_BY_KEYWORD,
                params={"keyword": keywords},
                headers={"Content_type": "application/json", "X-API-KEY": API_KEY}
            ).json()
        
        return response



class Interface:
    #Пользовател выбирает номер жанра
    def user_chooses_a_genre():
        genres = Interface.show_a_list_of_genres()
        while True:
            selected_genre = input("Введитец цифру: ")
            
            if checking_whether_a_number_is_entered_by_the_user(selected_genre):
                selected_genre = int(selected_genre)
                #Проверка есть ли это число в списке жанров, которые показываются пользователю
                if GenreApiHandler.checking_whether_a_genre_exists(selected_genre=selected_genre, all_genres=genres):
                    return selected_genre
                else:
                    print('Вы ввели цифру, которая не находится в списке!')
               
    #вывод фильмов по выбранному пользователем жанру
    def output_of_films_by_the_selected_genre(id_genre: int):
        genre: int = id_genre
        films_hash: dict = GenreApiHandler.api_request_by_genre(genre=genre)

        films = GenreApiHandler.unpacking_the_movie_request_api(films_data=films_hash)
        for film in films:
            print(f"{film}\n")
    
    #Вывод жанров в терминал
    def output_of_genres_to_the_terminal(data_genre:list):
        for id, genre in data_genre:
            print(f"{id}. {genre}")

    #Показывать список жанров
    def show_a_list_of_genres():
        print("Cписок жанров: ")
        genres: list = we_get_all_genres()
        Interface.output_of_genres_to_the_terminal(genres)
        return genres


    # #Метод поиска по названию 1
    # def name_search_method():
    #     movie_keywords: str = str(input("Введите ключевые слова, для поиска фильмов:\n"))
    #     movie_data = GenreApiHandler.get_movies_by_keywords(keywords=movie_keywords)
    #     print(movie_data)
        
    #     new_data_items = sorted(movie_data, key=lambda film: film["year"])
    #     sorted_data |= new_data_items
    #     films = GenreApiHandler.unpacking_the_movie_request_api(films_data=sorted_data)
    #     for film in film:
    #         print(f"{film}\n")

    # Метод поиска по названию 2
    def name_search_method():
        movie_keywords: str = str(input("Введите ключевые слова, для поиска фильмов:\n"))
        movie_data = GenreApiHandler.get_movies_by_keywords(keywords=movie_keywords)
        #print(movie_data)
        
        # Check if each element in movie_data is a dictionary and if the "year" key exists
        new_data_items = sorted(movie_data["films"], key=lambda film: film["year"])
        sorted_data = new_data_items
        
        films = GenreApiHandler.unpacking_the_movie_request_api_for_search_name(films_data=sorted_data, pagescount=movie_data["pagesCount"])
        for film in films:
            print(f"{film}\n")    
        


#Проверка вводит ли пользователь число
def checking_whether_a_number_is_entered_by_the_user(selected_genre):
    try:
        number = int(selected_genre)

        if isinstance(number, int):
            print("Вы ввели число.")
            return True

    except ValueError:
        print("Вы не ввели число.")
        return False

#Получаем все страницы топовых фильмов
def get_all_the_top_movie_pages():
    top_films: list = []
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
    

#вывод всех жанров
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
        if genre_hash["genre"] != "":
            all_genres.append([genre_hash["id"], genre_hash["genre"]])
        
    
    return all_genres

def main():
    # test: int = Interface.user_chooses_a_genre()
    # Interface.output_of_films_by_the_selected_genre(id_genre=test)
    Interface.name_search_method()
    

if __name__ == "__main__":
    main()
#Film.genre(we_get_all_genres())

# for film in get_all_the_top_movie_pages():
#      print(f"{film}\n")

