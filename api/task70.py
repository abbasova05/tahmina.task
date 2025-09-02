from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)
CSV_FILE = 'reyler.csv'

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Restoran Rəyləri</title>
</head>
<body>
    <h2> Restoranımız haqqında fikrinizi bölüşün</h2>
    <form method="POST">
        <label>Adınız:</label><br>
        <input type="text" name="ad" required><br><br>

        <label>Ən bəyəndiyiniz yemək:</label><br>
        <select name="yemek" required>
            <option value="">Seçin</option>
            <option value="Dolma">Dolma</option>
            <option value="Kabab">Kabab</option>
            <option value="Plov">Plov</option>
            <option value="Düşbərə">Düşbərə</option>
            <option value="Şorba">Şorba</option>
        </select><br><br>

        <label>Qısa rəyiniz:</label><br>
        <textarea name="rey" rows="4" cols="40" placeholder="Rəyinizi yazın..." required></textarea><br><br>

        <input type="submit" value="Göndər">
    </form>

    {% if mesaj %}
        <hr>
        <h3 style="color:green;">{{ mesaj }}</h3>
        <p><strong>Ad:</strong> {{ ad }}</p>
        <p><strong>Yemək:</strong> {{ yemek }}</p>
        <p><strong>Rəy:</strong><br>{{ rey }}</p>
    {% endif %}
</body>
</html>
'''

def yaz_csv(ad, yemek, rey):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([ad, yemek, rey])

@app.route('/', methods=['GET', 'POST'])
def index():
    mesaj = ''
    ad = yemek = rey = ''
    if request.method == 'POST':
        ad = request.form.get('ad')
        yemek = request.form.get('yemek')
        rey = request.form.get('rey')
        yaz_csv(ad, yemek, rey)
        mesaj = "Rəyiniz qeydə alındı. Təşəkkür edirik!"
    return render_template_string(html, mesaj=mesaj, ad=ad, yemek=yemek, rey=rey)

if __name__ == '__main__':
    app.run(debug=True)
