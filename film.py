

class Film:

    def __init__(self, film_hash):
        self.title = film_hash["nameRu"]
        self.year = film_hash["year"]
        self.rating = film_hash["rating"]
        self.genres: list = film_hash["genres"] 
        self.description = film_hash["description"]
        self.countries = film_hash["countries"]
        

        

    def __str__(self):
        return f"Название: {self.title}\nГод: {self.year}\nРейтинг: {self.rating}"
    
