from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)
CSV_FILE = 'sifarisler.csv'

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Kitab Sifarişi</title>
</head>
<body>
    <h2>Kitab sifarişi formu</h2>
    <form method="POST">
        <label>Kitabın adı:</label>
        <input type="text" name="kitab" required><br><br>

        <label>Müəllif:</label>
        <input type="text" name="muellif" required><br><br>

        <label>Əlaqə nömrəsi:</label>
        <input type="tel" name="telefon" placeholder="+994 XX XXX XX XX" pattern="[+0-9\\s\\-]+" required><br><br>

        <input type="submit" value="Sifariş et">
    </form>

    {% if mesaj %}
        <hr>
        <h3 style="color:green;">{{ mesaj }}</h3>
        <p><strong>Kitab:</strong> {{ kitab }}</p>
        <p><strong>Müəllif:</strong> {{ muellif }}</p>
        <p><strong>Əlaqə:</strong> {{ telefon }}</p>
    {% endif %}
</body>
</html>
'''

def yaz_csv(kitab, muellif, telefon):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([kitab, muellif, telefon])

@app.route('/', methods=['GET', 'POST'])
def index():
    mesaj = ''
    kitab = muellif = telefon = ''
    if request.method == 'POST':
        kitab = request.form.get('kitab')
        muellif = request.form.get('muellif')
        telefon = request.form.get('telefon')
        yaz_csv(kitab, muellif, telefon)
        mesaj = "Sifarişiniz qeydə alındı."
    return render_template_string(html, mesaj=mesaj, kitab=kitab, muellif=muellif, telefon=telefon)

if __name__ == '__main__':
    app.run(debug=True)
