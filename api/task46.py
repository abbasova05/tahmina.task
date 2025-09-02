from flask import Flask, jsonify, request

app = Flask(__name__)

notes = [
    {'id': 1, 'content': 'Sabah görüş var'},
    {'id': 2, 'content': 'Kitabxanaya get'},
]

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes), 200

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    content = data.get('content') if data else None
    if not content:
        return jsonify({"error": "Qeyd məzmununu göndərin"}), 400

    new_id = notes[-1]['id'] + 1 if notes else 1
    note = {'id': new_id, 'content': content}
    notes.append(note)
    return jsonify(note), 201

if __name__ == '__main__':
    app.run(debug=True)
