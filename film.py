class Film:

    @staticmethod
    def genre(data_genre:list):
        for id, genre in data_genre:
            print(f"{id}. {genre}")

    def __init__(self, film_hash):
        self.title = film_hash["nameRu"]
        self.year = film_hash["year"]
        genre = []

    def __str__(self):
        return f"Название: {self.title}\nГод: {self.year}"
    
class Genres:
    def __init__(self, genre_hash):
        self.id = genre_hash["id"]
        self.genre = genre_hash["genre"]
    
    def __str__(self):
        return f"{self.id}. {self.genre}"