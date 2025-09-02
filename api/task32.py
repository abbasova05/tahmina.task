from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

def find_user(user_id):
    return next(( user for user in users if user['id'] == user_id), None)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(user)
    return jsonify(user), 201

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = find_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 200

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    user = find_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    user['name'] = data.get('name', user['nmae'])
    user['email'] = data.get('email', user['email'])

    return jsonify(user), 200

if __name__ == '__main__':
    app.run(debug=True)

    