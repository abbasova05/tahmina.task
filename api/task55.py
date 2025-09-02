from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = []

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': user_data.get('name'),
        'email': user_data.get('email')
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    global users
    original_len = len(users)
    users = [u for u in users if u['id'] != user_id]
    if len(users) == original_len:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User deleted'}), 200

@app.route('/users/view')
def view_users():
    return render_template('bilmemnecenci.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
