from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)
CSV_FILE = 'teklifler.csv'

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Təklif formu</title>
</head>
<body>
    <h2>İdeya və ya təklifinizi göndərin</h2>
    <form method="POST">
        <label>Adınız:</label>
        <input type="text" name="ad" required><br><br>

        <label>E-poçt:</label>
        <input type="email" name="email" required><br><br>

        <label>Təklif və ya ideyanız:</label><br>
        <textarea name="teklif" rows="5" cols="40" placeholder="Buraya yazın..." required></textarea><br><br>

        <input type="submit" value="Göndər">
    </form>

    {% if mesaj %}
        <hr>
        <h3 style="color:green;">{{ mesaj }}</h3>
        <p><strong>Ad:</strong> {{ ad }}</p>
        <p><strong>E-poçt:</strong> {{ email }}</p>
        <p><strong>Təklif:</strong><br>{{ teklif }}</p>
    {% endif %}
</body>
</html>
'''

def yaz_teklif_csv(ad, email, teklif):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([ad, email, teklif])

@app.route('/', methods=['GET', 'POST'])
def index():
    mesaj = ''
    ad = email = teklif = ''
    if request.method == 'POST':
        ad = request.form.get('ad')
        email = request.form.get('email')
        teklif = request.form.get('teklif')
        yaz_teklif_csv(ad, email, teklif)
        mesaj = "Təklifiniz uğurla göndərildi. Təşəkkür edirik!"
    return render_template_string(html, mesaj=mesaj, ad=ad, email=email, teklif=teklif)

if __name__ == '__main__':
    app.run(debug=True)
