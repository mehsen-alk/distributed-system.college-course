import grpc
import movies_pb2
import movies_pb2_grpc


def run():
    with grpc.insecure_channel('192.168.43.220:8000') as channel:
        stub = movies_pb2_grpc.MovieServiceStub(channel)

        while True:
            choice = input("Enter your choice: ")

            if choice == '1':
                response = stub.GetMoviesTitle(movies_pb2.MovieTitleRequest())
                print(response.titles)

            elif choice == '2':
                title = input("Enter movie title: ")
                director = input("Enter movie director: ")
                release_year = int(input("Enter movie release year: "))
                genre = input("Enter movie genre: ")

                response = stub.AddMovie(movies_pb2.AddMovieRequest(
                    title=title,
                    director=director,
                    release_year=release_year,
                    genre=genre
                ))
                print(response.message)

            elif choice == '3':
                title = input("Enter movie title: ")

                response = stub.LookupDate(movies_pb2.MovieLookupRequest(title=title))
                print(response.release_year)


if __name__ == "__main__":
    run()
