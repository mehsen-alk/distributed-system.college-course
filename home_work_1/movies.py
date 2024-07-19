import os

DB_PATH = 'movies_db.csv'


class Movie:
    def __init__(self, title, director, release_year, genre):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Release Year: {self.release_year}")
        print(f"Genre: {self.genre}")
        print(f"Average Rating: {self.average_rating()}")

    def rate(self):
        rating = float(input("Enter your rating for this movie (1-5): "))
        if 1 <= rating <= 5:
            self.add_rating(rating)
            print("Thank you for your rating!")
        else:
            print("Invalid rating. Please enter a rating between 1 and 5.")

    def average_rating(self):
        if not self.ratings:
            return 0

        avgSum = sum(self.ratings)
        return avgSum / len(self.ratings)

    def to_string(self):
        attributes = [self.title, self.director, str(
            self.release_year), self.genre, str(self.average_rating())]
        csv_string = ",".join(attributes)
        return csv_string


def initialize_db(db_name=DB_PATH):
    header_row = "Title,Director,Release Year, Genre, Average Rating"
    with open(db_name, 'w') as db:
        db.write(header_row)
        db.write('\n')
    print("Database Initialized.")


def add_to_db(movie, db_name=DB_PATH):
    with open(db_name, 'a') as db:
        db.write(movie.to_string())
        db.write('\n')
    print(f"{movie.title} added successfully.")


def askUserForMovie():
    # print('enter movie Title')
    movieName = input('enter movie Title: ')

    # print('enter movie Director')
    movieDirector = input('enter movie Director: ')

    # print('enter movie Release Year')
    movieReleaseYear = input('enter movie Release Year: ')

    # print('enter movie Genre')
    movieGenre = input('enter movie Genre: ')

    return Movie(movieName, movieDirector, movieReleaseYear, movieGenre)


def lookUp(title, db_name=DB_PATH):
    with open(db_name, 'r') as db:
        moviesR = db.readlines()

        for movieR in moviesR:
            movieInfo = movieR.split(',')
            if movieInfo[0].find(title) >= 0:
                return Movie(movieInfo[0], movieInfo[1], movieInfo[2], movieInfo[3])


def lookUpDate(title, db_name=DB_PATH):
    with open(db_name, 'r') as db:
        moviesR = db.readlines()

        for movieR in moviesR:
            movieInfo = movieR.split(',')
            if movieInfo[0].find(title) >= 0:
                return movieInfo[2]


def getMoviesTitle(db_name=DB_PATH):
    with open(db_name, 'r') as db:
        moviesR = db.readlines()

        titles = []

        for movieR in moviesR:
            movieInfo = movieR.split(',')
            titles.append(movieInfo[0])

        return titles


if __name__ == "__main__":

    if not os.path.isfile(DB_PATH):
        initialize_db()

    print(lookUp('The Avengers').to_string())
