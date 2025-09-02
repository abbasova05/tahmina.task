from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Gizli açar
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# Sadə istifadəçi məlumatı (mock database)
users = {
    "test@example.com": {
        "password": "123456",
        "name": "Test User"
    }
}

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = users.get(email)
    if not user or user['password'] != password:
        return jsonify({"msg": "Invalid email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

# Qorunan endpoint
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
