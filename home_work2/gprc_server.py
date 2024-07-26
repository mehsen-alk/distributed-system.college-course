from concurrent import futures
import grpc
import movies_pb2
import movies_pb2_grpc

from home_work_1 import movies


class MovieService(movies_pb2_grpc.MovieServiceServicer):
    def GetMoviesTitle(self, request, context):
        titles = movies.getMoviesTitle()
        return movies_pb2.MovieTitleResponse(titles=titles)

    def AddMovie(self, request, context):
        movie = movies.Movie(
            title=request.title,
            director=request.director,
            release_year=request.release_year,
            genre=request.genre
        )
        movies.add_to_db(movie)
        return movies_pb2.AddMovieResponse(message='204 no content')

    def LookupDate(self, request, context):
        release_year = movies.lookUpDate(request.title)
        return movies_pb2.MovieLookupResponse(release_year=int(release_year))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movies_pb2_grpc.add_MovieServiceServicer_to_server(MovieService(), server)
    server.add_insecure_port('192.168.43.220:8000')
    print("gRPC Server is running...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
