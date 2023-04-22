

class Film:

    @staticmethod
    #Вывод жанров в терминал
    def genre(data_genre:list):
        for id, genre in data_genre:
            print(f"{id}. {genre}")

    def __init__(self, film_hash):
        self.title = film_hash["nameRu"]
        self.year = film_hash["year"]
        genre = []

    def __str__(self):
        return f"Название: {self.title}\nГод: {self.year}"
    
