from flask import Flask, request, jsonify

app = Flask(__name__)

movies = []

def find_movie(movie_id):
    return next((movie for movie in movies if movie['id'] == movie_id), None)

@app.route("/movies", methods=["POST"])
def add_movie():
    data = request.get_json()
    if not data or 'title' not in data or 'director' not in data or 'year' not in data:
        return jsonify({'error': 'Title, director, and year are required'}), 400

    if not isinstance(data['year'], int) or data['year'] < 1888 or data['year'] > 2100:
        return jsonify({'error': 'Invalid year'}), 400

    for movie in movies:
        if movie['title'].lower() == data['title'].lower() and movie['director'].lower() == data['director'].lower():
            return jsonify({'error': 'This movie already exists'}), 400

    movie = {
        'id': len(movies) + 1,
        'title': data['title'],
        'director': data['director'],
        'year': data['year']
    }
    movies.append(movie)
    return jsonify(movie), 201

@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

@app.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = find_movie(movie_id)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    return jsonify(movie), 200

@app.route("/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    movie = find_movie(movie_id)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404

    movie['title'] = data.get('title', movie['title'])
    movie['director'] = data.get('director', movie['director'])
    movie['year'] = data.get('year', movie['year'])

    return jsonify(movie), 200

@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    global movies
    movie = find_movie(movie_id)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404

    movies = [m for m in movies if m['id'] != movie_id]
    return jsonify({'message': 'Movie deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)