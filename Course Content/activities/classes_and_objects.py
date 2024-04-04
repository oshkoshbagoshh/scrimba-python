# classes and objects

print("**Classes & Objects**")

# create a movie Class
class Movie:
    def __init__(self, title, year, imdb_score, have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen
    
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)
        

# create instance of classs        
film_1 = Movie("Life of Brian", 1979, 8.1, True)
film_2 = Movie("Holy Grail", 1975, 8.2, True)
films = [film_1,film_2]
print(films[0], films[1])
print(film_1.title, film_1.imdb_score)
film_1.nice_print()
film_2.nice_print()


