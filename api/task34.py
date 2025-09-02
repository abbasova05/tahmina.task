from flask import Flask, request, jsonify

app = Flask(__name__)

games = []

def find_game(game_id):
    return next((game for game in games if game['id'] == game_id), None)

@app.route("/games", methods=["POST"])
def add_game():
    data = request.get_json()
    if not data or 'title' not in data or 'genre' not in data or 'year' not in data:
        return jsonify({'error': 'Title, genre, and year are required'}), 400

    if not isinstance(data['year'], int) or data['year'] < 1970 or data['year'] > 2100:
        return jsonify({'error': 'Invalid year'}), 400

    for game in games:
        if game['title'].lower() == data['title'].lower() and game['genre'].lower() == data['genre'].lower():
            return jsonify({'error': 'This game already exists'}), 400

    game = {
        'id': len(games) + 1,
        'title': data['title'],
        'genre': data['genre'],
        'year': data['year']
    }
    games.append(game)
    return jsonify(game), 201

@app.route("/games", methods=["GET"])
def get_games():
    return jsonify(games), 200

@app.route("/games/<int:game_id>", methods=["GET"])
def get_game(game_id):
    game = find_game(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    return jsonify(game), 200

@app.route("/games/<int:game_id>", methods=["PUT"])
def update_game(game_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    game = find_game(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404

    game['title'] = data.get('title', game['title'])
    game['genre'] = data.get('genre', game['genre'])
    game['year'] = data.get('year', game['year'])

    if not isinstance(game['year'], int) or game['year'] < 1970 or game['year'] > 2100:
        return jsonify({'error': 'Invalid year'}), 400

    return jsonify(game), 200

@app.route("/games/<int:game_id>", methods=["DELETE"])
def delete_game(game_id):
    global games
    game = find_game(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404

    games = [g for g in games if g['id'] != game_id]
    return jsonify({'message': 'Game deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
