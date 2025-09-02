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

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user = request.args.get('user')
    users = load_users()

    if request.method == 'POST':
        new_ad = request.form.get('new_ad').strip()
        new_sifre = request.form.get('new_sifre').strip()

        old_user_data = users.get(user)

        if not old_user_data:
            return "İstifadəçi tapılmadı!"

        if new_ad and new_ad != user:
            if new_ad in users:
                return "Bu ad artıq mövcuddur!"
            
            users[new_ad] = old_user_data
            del users[user]
            user = new_ad  
        else:
            new_ad = user  

        
        if new_sifre:
            hashed = bcrypt.hashpw(new_sifre.encode('utf-8'), bcrypt.gensalt())
            users[new_ad] = hashed.decode('utf-8')

        save_users(users)
        return redirect(url_for('dashboard', user=new_ad))

    return render_template('dashboardd.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
