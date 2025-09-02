from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/', methods=['GET'])
def index():
    return render_template('formmm.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return render_template('resulttt.html', message="Ad və email daxil edilməlidir!")

    user = {'name': name, 'email': email}
    users.append(user)

    return render_template('resulttt.html', message=f"İstifadəçi əlavə olundu: {name} ({email})")

@app.route('/users', methods=['GET'])
def list_users():
    return render_template('users.html', users=users)

@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def api_add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name və email tələb olunur'}), 400
    
    user = {'name': data['name'], 'email': data['email']}
    users.append(user)
    return jsonify({'message': 'İstifadəçi əlavə olundu', 'user': user}), 201

@app.route('/api/users/<email>', methods=['DELETE'])
def api_delete_user(email):
    global users
    users = [u for u in users if u['email'] != email]
    return jsonify({'message': f'{email} email-li istifadəçi silindi.'})

if __name__ == '__main__':
    app.run(debug=True)
