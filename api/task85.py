from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_jwt_demo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Home Route
@app.route('/')
def home():
    return "API is running..."

# Register Route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists'}), 400

    hashed_pw = generate_password_hash(data['password'])
    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        password=hashed_pw
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    token = create_access_token(identity=user.public_id, expires_delta=timedelta(hours=1))
    return jsonify({'token': token}), 200

# Protected Route
@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': f'Welcome {user.name}! This is your dashboard.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
