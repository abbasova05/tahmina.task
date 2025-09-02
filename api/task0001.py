from flask import Flask, request, render_template
import csv
import re

app = Flask(__name__)

def email_dogru_formatda(email):
    # Sadə email yoxlama regex
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def save_to_csv(username, password, email):
    with open('qeydiyyatlar.csv', mode='a', newline='', encoding='utf-8') as fayl:
        writer = csv.writer(fayl)
        writer.writerow([username, password, email])

@app.route('/', methods=['GET', 'POST'])
def qeydiyyat():
    mesaj = None
    ugurlu = None
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        email = request.form.get('email', '').strip()
        
        # Yoxlamalar
        if not username:
            mesaj = "İstifadəçi adı boş ola bilməz!"
        elif not email_dogru_formatda(email):
            mesaj = "Email düzgün formatda deyil!"
        else:
            # Hamısı düzgündür, CSV-ə yaz
            save_to_csv(username, password, email)
            ugurlu = "Qeydiyyat uğurla tamamlandı!"
    
    return render_template("qeydiyyat.html", mesaj=mesaj, ugurlu=ugurlu, request=request)

if __name__ == "__main__":
    app.run(port=1453, debug=True, host="0.0.0.0")