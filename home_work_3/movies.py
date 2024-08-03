import os
import csv


DB_PATH = 'movies_db.csv'


class Movie:
    def __init__(self, id, title, director, release_year, genre):
        self.id = id
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def display_info(self):
        print(f"Id: {self.id}")
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
        attributes = [str(self.id), self.title, self.director, str(
            self.release_year), self.genre, str(self.average_rating())]
        csv_string = ",".join(attributes)
        return csv_string

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "director": self.director,
            "genre": self.genre,
            "release_year": self.release_year,
        }


def initialize_db(db_name=DB_PATH):
    header_row = "id,title,director,release_year,genre"
    with open(db_name, 'w') as db:
        db.write(header_row)
        db.write('\n')
    print("Database Initialized.")


def add_to_db(movie, db_name=DB_PATH):
    with open(db_name, 'r') as db:
        moviesList = db.readlines()
        lastMovie = moviesList[-1]

        newMovieId = 1

        if lastMovie is not None:
            movieInfo = lastMovie.split(',')
            if movieInfo[0].strip().lower() != 'id':
                newMovieId = int(movieInfo[0]) + 1

        movie.id = newMovieId

    with open(db_name, 'a') as db:
        db.write(movie.to_string())
        db.write('\n')
    print(f"{movie.title} added successfully.")


def update_movie(id, movie, db_name=DB_PATH):
    records = []
    record_found = False

    with open(db_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(id):
                row.update(
                    {
                        'title': movie.title,
                        'director': movie.director,
                        'release_year': movie.release_year,
                        'genre': movie.genre
                    }
                )
                record_found = True
            records.append(row)

    if not record_found:
        print(f"Record with ID {id} not found.")
        return False  # Return False or handle as needed

    with open(db_name, mode='w', newline='') as file:
        fieldnames = records[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    return True


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
            if movieInfo[1] == title:
                return Movie(movieInfo[0], movieInfo[1], movieInfo[2], movieInfo[3], movieInfo[4])


def lookUpDate(date, db_name=DB_PATH):
    with open(db_name, 'r') as db:
        moviesR = db.readlines()

        for movieR in moviesR:
            movieInfo = movieR.split(',')
            if movieInfo[3] == date:
                return movieInfo[1]
            else:
                return 404


def lookUpDirector(director, db_name=DB_PATH):
    with open(db_name, 'r') as db:
        moviesR = db.readlines()

        moviesList = []

        for movieR in moviesR:
            movieInfo = movieR.split(',')
            if movieInfo[2] == director:
                moviesList.append(movieR)

        return moviesList


def getMoviesTitle(db_name=DB_PATH):
    with open(db_name, 'r') as db:
        moviesR = db.readlines()

        titles = []

        titleRemoved = False

        for movieR in moviesR:
            if not titleRemoved:
                titleRemoved = True
                continue

            movieInfo = movieR.split(',')
            titles.append(movieInfo[1])

        return titles


def init():
    if not os.path.isfile(DB_PATH):
        initialize_db()


if __name__ == "__main__":

    if not os.path.isfile(DB_PATH):
        initialize_db()

    print(lookUp('The Avengers').to_string())
