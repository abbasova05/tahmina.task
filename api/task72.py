from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        ad = request.form['ad']
        sifre = request.form['sifre']
        users = load_users()

        if ad in users:
            return "Bu istifadəçi artıq mövcuddur!"

        users[ad] = sifre
        save_users(users)
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ad = request.form['ad']
        sifre = request.form['sifre']
        users = load_users()

        if ad in users and users[ad] == sifre:
            return redirect(url_for('dashboard', user=ad))
        else:
            return "Ad və ya şifrə səhvdir!"
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    user = request.args.get('user')
    return render_template('dashboard.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
