import xmlrpc.server

from home_work_1 import movies


class MovieServer:
    def get_movies_title(self):
        return movies.getMoviesTitle()

    def add_movie(self, title, director, release_year, genre):
        movie = movies.Movie(title, director, release_year, genre)
        movies.add_to_db(movie)
        return '204 no content'

    def lookup_date(self, title):
        return movies.lookUpDate(title)

server = xmlrpc.server.SimpleXMLRPCServer(("192.168.43.220", 8000))
server.register_instance(MovieServer())

print("XML-RPC Server is running...")
server.serve_forever()
