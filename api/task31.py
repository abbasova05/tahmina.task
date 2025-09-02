from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'year' not in data:
        return jsonify({'error': 'Title, author, and year are required'}), 400
    
    if not isinstance(data['year'], int) or data['year'] < 0 or data['year'] > 2100:
        return jsonify({'error': 'Invalid year'}), 400

    for book in books:
        if book['title'] == data['title'] and book['author'] == data['author']:
            return jsonify({'error': 'This book already exists'}), 400

    book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author'],
        'year': data['year']
    }
    books.append(book)
    return jsonify(book), 201

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book), 200

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    book = find_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    book['year'] = data.get('year', book['year'])

    return jsonify(book), 200

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    book = find_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
