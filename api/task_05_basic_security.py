from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from datetime import timedelta

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

# İstifadəçi məlumatları yaddaşda
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Basic Authentication
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT Authentication
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token_data = {
        "username": username,
        "role": user["role"]
    }
    access_token = create_access_token(identity=token_data)
    return jsonify(access_token=access_token), 200

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    user_data = get_jwt_identity()
    if user_data["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# ---------------------
# JWT Error Handlers
# ---------------------
@jwt.unauthorized_loader
def unauthorized_callback(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run()