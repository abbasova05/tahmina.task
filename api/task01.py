from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)

# Form və nəticələr üçün HTML şablonu
form_html = '''
<!DOCTYPE html>
<html>
<head><title>Əlaqə Forması</title></head>
<body>
    <h2>Əlaqə Formu</h2>
    {% if mesaj %}
        <p style="color: green;">{{ mesaj }}</p>
    {% endif %}
    <form method="POST">
        Ad: <input type="text" name="ad" value="{{ request.form.ad or '' }}"><br><br>
        Email: <input type="text" name="email" value="{{ request.form.email or '' }}"><br><br>
        Mesaj: <br>
        <textarea name="mesaj" rows="4" cols="40">{{ request.form.mesaj or '' }}</textarea><br><br>
        <input type="submit" value="Göndər">
    </form>
    <br>
    <a href="/contacts">Bütün əlaqələrə bax</a>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    mesaj = ""
    if request.method == 'POST':
        ad = request.form.get('ad', '').strip()
        email = request.form.get('email', '').strip()
        mesaj_metin = request.form.get('mesaj', '').strip()

        # Sadə yoxlama: boş olmasın
        if ad and email and mesaj_metin:
            # CSV-ə yaz
            with open('contacts.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([ad, email, mesaj_metin])
            mesaj = "Məlumatınız uğurla göndərildi!"
        else:
            mesaj = "Zəhmət olmasa, bütün sahələri doldurun."

    return render_template_string(form_html, mesaj=mesaj, request=request)

@app.route('/contacts')
def contacts():
    contacts = []
    try:
        with open('contacts.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            contacts = list(reader)
    except FileNotFoundError:
        contacts = []

    # Sadə HTML siyahısı ilə göstərək
    contacts_html = '''
    <!DOCTYPE html>
    <html>
    <head><title>Bütün Əlaqələr</title></head>
    <body>
        <h2>Bütün Əlaqə Məlumatları</h2>
        <a href="/">Əlaqə formuna qayıt</a><br><br>
        {% if contacts %}
            <table border="1" cellpadding="5" cellspacing="0">
                <tr><th>Ad</th><th>Email</th><th>Mesaj</th></tr>
                {% for ad, email, mesaj in contacts %}
                <tr>
                    <td>{{ ad }}</td>
                    <td>{{ email }}</td>
                    <td>{{ mesaj }}</td>
                </tr>
                {% endfor %}
            </table>
        {% else %}
            <p>Heç bir məlumat yoxdur.</p>
        {% endif %}
    </body>
    </html>
    '''
    return render_template_string(contacts_html, contacts=contacts)

if __name__ == '__main__':
    app.run(port=1453, debug=True, host="0.0.0.0")
