from flask import Flask, request, render_template, redirect
import csv
import os

app = Flask(__name__)

CSV_FILE = 'users.csv'

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'password'])

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return "Zəhmət olmasa bütün xanaları doldurun", 400

        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username:
                    return "Bu istifadəçi artıq mövcuddur", 400

        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        return redirect('/success')

    return render_template('registerr.html')

@app.route('/success')
def success():
    return "Qeydiyyat uğurla tamamlandı!"

if __name__ == '__main__':
    app.run(debug=True)
