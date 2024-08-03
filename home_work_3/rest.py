from flask import Flask, jsonify, request
import movies as m

app = Flask(__name__)


@app.route('/')
def isServerRunning():
    return "server is up and running"


@app.route('/moviesTitle')
def getTitle():
    moviesTitle = m.getMoviesTitle()
    return jsonify({"movies": moviesTitle})


@app.route('/movie', methods=['POST'])
def add_movie():
    data = request.get_json()

    try:
        title = data['title']
        director = data['director']
        release_year = int(data['release_year'])
        genre = data['genre']
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e.args[0]}"}), 400
    except ValueError:
        return jsonify({"error": "Invalid value for release_year; it must be an integer"}), 400

    if not title or not director or not release_year or not genre:
        return jsonify({"error": "All fields (title, director, release_year, genre) are required"}), 400

    movie = m.Movie(id=-1, title=title, director=director,
                    release_year=release_year, genre=genre)

    m.add_to_db(movie=movie)

    return jsonify({"msg": "Movie added successfully"}), 201


@app.route('/movie')
def getMovie():
    title = request.args.get('title')

    if not title:
        return jsonify({"msg": "title is required"}), 400

    movie = m.lookUp(title=title)

    if not movie:
        return jsonify({"msg": "not found"}), 404

    return jsonify(movie.to_json()), 200


@app.route('/movie', methods=['PUT'])
def update_movie():
    data = request.get_json()

    try:
        id = data['id']
        title = data['title']
        director = data['director']
        release_year = int(data['release_year'])
        genre = data['genre']
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e.args[0]}"}), 400
    except ValueError:
        return jsonify({"error": "Invalid value for id or release_year; it must be an integer"}), 400

    if not id or not title or not director or not release_year or not genre:
        return jsonify({"error": "All fields (title, director, release_year, genre) are required"}), 400

    movie = m.Movie(id=id, title=title, director=director,
                    release_year=release_year, genre=genre)

    if m.update_movie(id=id, movie=movie):
        return jsonify({"msg": "Movie updated successfully"}), 204

    return jsonify({"msg": "Movie Not Found"}), 404


@app.route('/movieDirector')
def getDirectorMovies():
    director = request.args.get('director')

    if not director:
        return jsonify({"msg": "director is required"}), 400

    movie = m.lookUpDirector(director=director)

    if not movie:
        return jsonify({"msg": "not found"}), 404

    return jsonify({"movies": movie}), 200


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=1233)
    m.init()
