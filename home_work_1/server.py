import socket
import movies
import pickle


port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', port))

s.listen()

print('server is up')

conn, addr = s.accept()
while True:
    msg = conn.recv(1024)

    msg = pickle.loads(msg)

    print('got request: ', msg)

    choice = msg[0]

    if (choice == '1'):
        conn.send(pickle.dumps(movies.getMoviesTitle()))

    if (choice == '2'):
        title = msg[1]
        director = msg[2]
        release_year = msg[3]
        genre = msg[4]

        movie = movies.Movie(title, director, release_year, genre)

        movies.add_to_db(movie)

        conn.send(pickle.dumps('204 no content'))

    if (choice == '3'):
        title = msg[1]

        movieReleaseDate = movies.lookUpDate(title)

        conn.send(pickle.dumps(movieReleaseDate))
