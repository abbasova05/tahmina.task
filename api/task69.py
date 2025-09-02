from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)
CSV_FILE = 'filmler.csv'

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Film Tövsiyəsi</title>
</head>
<body>
    <h2>Sevdiyiniz filmi bizimlə paylaşın 🎬</h2>
    <form method="POST">
        <label>Adınız:</label><br>
        <input type="text" name="ad" required><br><br>

        <label>Film adı:</label><br>
        <input type="text" name="film" required><br><br>

        <label>Niyə bu filmi tövsiyə edirsiniz?</label><br>
        <textarea name="fikr" rows="5" cols="40" placeholder="Buraya səbəbinizi yazın..." required></textarea><br><br>

        <input type="submit" value="Göndər">
    </form>

    {% if mesaj %}
        <hr>
        <h3 style="color:green;">{{ mesaj }}</h3>
        <p><strong>Ad:</strong> {{ ad }}</p>
        <p><strong>Film:</strong> {{ film }}</p>
        <p><strong>Fikrin:</strong><br>{{ fikr }}</p>
    {% endif %}
</body>
</html>
'''

def yaz_film(ad, film, fikr):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([ad, film, fikr])

@app.route('/', methods=['GET', 'POST'])
def index():
    mesaj = ''
    ad = film = fikr = ''
    if request.method == 'POST':
        ad = request.form.get('ad')
        film = request.form.get('film')
        fikr = request.form.get('fikr')
        yaz_film(ad, film, fikr)
        mesaj = "Tövsiyəniz qeyd edildi. Təşəkkürlər!"
    return render_template_string(html, mesaj=mesaj, ad=ad, film=film, fikr=fikr)

if __name__ == '__main__':
    app.run(debug=True)
