from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.secret_key = "supersecretkey"
users = {}
@app.route('/')
def home():
    if 'username' in session:
        return render_template('bash.html', username=session['username'])
    return redirect(url_for('login'))
@app.route('/qebul', methods=['GET', 'POST'])
def qebul():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Bu istifadeci adi artiq movcuddur!', 'error')
            return redirect(url_for('qebul'))
        hashed_password = generate_password_hash(password)
        users[username] = hashed_password
        flash('Qeydiyyat ugurla tamamlandi! İndi daxil ola bilersiniz.', 'success')
        return redirect(url_for('login'))
    return render_template('qebul1.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_password_hash = users.get(username)
        if user_password_hash and check_password_hash(user_password_hash, password):
            session['username'] = username
            flash('Xoş gelmisiniz, ' + username + '!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Istifadeci adi ve ya sifre sehvdir!', 'error')
            return redirect(url_for('login'))
    return render_template('login1.html')
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Siz cixis etdiniz.', 'info')
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)