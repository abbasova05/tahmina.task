from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = {
        'id': len(users) + 1,
        'name': data.get('name'),
        'email': data.get('email')
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'İstifadəçi silindi'}), 200

if __name__ == '__main__':
    app.run(debug=True)
