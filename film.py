

class Film:

    def __init__(self, film_hash):
        self.title = film_hash["nameRu"]
        self.year = film_hash["year"]
        self.genres: list = film_hash["genres"] 
        

    def __str__(self):
        return f"Название: {self.title}\nГод: {self.year}"
    
