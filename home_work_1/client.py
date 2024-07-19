import socket
import pickle


host = '192.168.1.100'
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))


while True:
    choice = input('enter your choice: ')

    if (choice == '1'):
        s.send(pickle.dumps(['1']))

    if (choice == '2'):
        title = input('enter movie title: ')
        director = input('enter movie director: ')
        release_year = input('enter movie release_year: ')
        genre = input('enter movie genre: ')

        s.send(pickle.dumps([choice, title, director, release_year, genre]))

    if (choice == '3'):
        title = input('enter movie title: ')

        s.send(pickle.dumps([choice, title]))

    msg = pickle.loads(s.recv(1024))

    print(msg)
