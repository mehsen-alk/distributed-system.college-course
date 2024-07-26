import xmlrpc.client

server_url = "http://192.168.43.220:8000"
server = xmlrpc.client.ServerProxy(server_url)

while True:
    choice = input("Enter your choice: ")

    if choice == '1':
        movies_titles = server.get_movies_title()
        print(movies_titles)

    elif choice == '2':
        title = input("Enter movie title: ")
        director = input("Enter movie director: ")
        release_year = input("Enter movie release year: ")
        genre = input("Enter movie genre: ")

        response = server.add_movie(title, director, release_year, genre)
        print(response)

    elif choice == '3':
        title = input("Enter movie title: ")
        release_date = server.lookup_date(title)
        print(release_date)
