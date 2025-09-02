from flask import Flask, jsonify, request

app = Flask(__name__)

# Başlanğıcda boş istifadəçilər
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    # İstifadəçi adlarının siyahısını JSON şəklində qaytar
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Əgər username artıq varsa, onu yenilə (istəyə görə dəyişə bilərsən)
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()