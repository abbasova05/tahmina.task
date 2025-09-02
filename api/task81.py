from flask import Flask, request, render_template, redirect, url_for
import csv, os

app = Flask(__name__)
CSV_FILE = 'users.csv'

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'password'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()


        if action == 'login':
            with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'] == username and row['password'] == password:
                        return redirect(url_for('success'))

            return "Login uğursuz oldu — istifadəçi adı və ya şifrə səhvdir", 400

        elif action == 'register':
            return redirect(url_for('register'))

    return render_template('indexi.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            return "Boş sahə ola bilməz", 400

        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if any(row['username'] == username for row in reader):
                return "Bu istifadəçi adı artıq istifadə olunur", 400

        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        return redirect(url_for('success'))
    return render_template('registerrr.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        new_username = request.form.get('new_username', '').strip()
        new_password = request.form.get('new_password', '').strip()

        if not username or (not new_username and not new_password):
            return "Zəhmət olmasa bütün məlumatları doldurun", 400

        users = []
        updated = False
        duplicate = False

        with open(CSV_FILE, 'r', newline='', encoding='utf‑8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username:
                    updated = True
                    continue
                if new_username and row['username'] == new_username:
                    duplicate = True
                users.append(row)

        if not updated:
            return "İstifadəçi tapılmadı", 404
        if duplicate:
            return "Yeni istifadəçi adı artıq mövcuddur", 400

        users.append({
            'username': new_username if new_username else username,
            'password': new_password if new_password else row['password']
        })

        with open(CSV_FILE, 'w', newline='', encoding='utf‑8') as file:
            writer = csv.DictWriter(file, fieldnames=['username','password'])
            writer.writeheader()
            writer.writerows(users)

        return "Məlumatlar yeniləndi"
    return render_template('updatee.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        users = []
        deleted = False

        with open(CSV_FILE, 'r', newline='', encoding='utf‑8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username:
                    deleted = True
                    continue
                users.append(row)

        if not deleted:
            return "İstifadəçi tapılmadı", 404

        with open(CSV_FILE, 'w', newline='', encoding='utf‑8') as file:
            writer = csv.DictWriter(file, fieldnames=['username','password'])
            writer.writeheader()
            writer.writerows(users)
        return "İstifadəçi silindi"
    return render_template('delete.html')

@app.route('/success')
def success():
    return "Xoş gəlmisiniz! Siz uğurla daxil oldunuz və ya qeydiyyatdan keçdiniz."

if __name__ == '__main__':
    app.run(debug=True)
