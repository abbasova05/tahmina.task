from flask import Flask, request, render_template_string, redirect, url_for
import csv
import os

app = Flask(__name__)
CSV_FILE = 'oyunlar.csv'

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Oyun Fikirləri</title>
</head>
<body>
    <h2> Sevdiyiniz oyunu bizimlə paylaşın</h2>

    <p>
        <a href="/"> Tövsiyə əlavə et</a> |
        <a href="/?mode=put"> Tövsiyə yenilə</a> |
        <a href="/?mode=delete"> Tövsiyə sil</a>
    </p>

    {% if mode == 'post' %}
        <h3>Yeni Tövsiyə Əlavə Et</h3>
        <form method="POST">
            <input type="hidden" name="method" value="post">
            <label>Adınız:</label><br>
            <input type="text" name="ad" required><br><br>
            <label>Oyun adı:</label><br>
            <input type="text" name="oyun" required><br><br>
            <label>Kateqoriya:</label><br>
            <input type="text" name="kateqori" required><br><br>
            <label>Fikriniz:</label><br>
            <textarea name="fikr" required></textarea><br><br>
            <input type="submit" value="Göndər">
        </form>
    {% elif mode == 'put' %}
        <h3> Tövsiyəni Yenilə</h3>
        <form method="POST">
            <input type="hidden" name="method" value="put">
            <label>Adınız:</label><br>
            <input type="text" name="ad" required><br><br>
            <label>Oyun adı:</label><br>
            <input type="text" name="oyun" required><br><br>
            <label>Kateqoriya:</label><br>
            <input type="text" name="kateqori" required><br><br>
            <label>Yeni fikir:</label><br>
            <textarea name="fikr" required></textarea><br><br>
            <input type="submit" value="Yenilə">
        </form>
    {% elif mode == 'delete' %}
        <h3> Tövsiyəni Sil</h3>
        <form method="POST">
            <input type="hidden" name="method" value="delete">
            <label>Adınız:</label><br>
            <input type="text" name="ad" required><br><br>
            <label>Oyun adı:</label><br>
            <input type="text" name="oyun" required><br><br>
            <label>Kateqoriya:</label><br>
            <input type="text" name="kateqori" required><br><br>
            <input type="submit" value="Sil">
        </form>
    {% endif %}

    {% if mesaj %}
        <hr>
        <h3 style="color:green;">{{ mesaj }}</h3>
        {% if ad and oyun %}
            <p><strong>Ad:</strong> {{ ad }}</p>
            <p><strong>Oyun:</strong> {{ oyun }}</p>
            <p><strong>Kateqoriya:</strong> {{ kateqori }}</p>
            {% if fikr %}
                <p><strong>Fikriniz:</strong> {{ fikr }}</p>
            {% endif %}
        {% endif %}
    {% endif %}
</body>
</html>
'''

def oxu_oyunlar():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        return list(csv.reader(f))

def yaz_oyun(ad, oyun, kateqori, fikr):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([ad, oyun, kateqori, fikr])

def overwrite_oyunlar(oyunlar):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(oyunlar)

@app.route('/', methods=['GET', 'POST'])
def index():
    mesaj = ''
    ad = oyun = kateqori = fikr = ''
    mode = request.args.get('mode', 'post')  

    if request.method == 'POST':
        method = request.form.get('method', 'post')
        ad = request.form.get('ad')
        oyun = request.form.get('oyun')
        kateqori = request.form.get('kateqori')
        fikr = request.form.get('fikr', '')

        oyunlar = oxu_oyunlar()

        if method == 'post':
            yaz_oyun(ad, oyun, kateqori, fikr)
            mesaj = "Tövsiyəniz əlavə edildi."

        elif method == 'put':
            updated = False
            for i, row in enumerate(oyunlar):
                if row[0] == ad and row[1] == oyun and row[2] == kateqori:
                    oyunlar[i] = [ad, oyun, kateqori, fikr]
                    updated = True
                    break
            if updated:
                overwrite_oyunlar(oyunlar)
                mesaj = "Tövsiyə uğurla yeniləndi."
            else:
                mesaj = "Yenilənəcək tövsiyə tapılmadı."

        elif method == 'delete':
            original_len = len(oyunlar)
            oyunlar = [row for row in oyunlar if not (row[0] == ad and row[1] == oyun and row[2] == kateqori)]
            if len(oyunlar) < original_len:
                overwrite_oyunlar(oyunlar)
                mesaj = "Tövsiyə uğurla silindi."
                fikr = ''
            else:
                mesaj = "Silinəcək tövsiyə tapılmadı."

        return redirect(url_for('index', mode=method, mesaj=mesaj, ad=ad, oyun=oyun, kateqori=kateqori, fikr=fikr))

    mesaj = request.args.get('mesaj', '')
    ad = request.args.get('ad', '')
    oyun = request.args.get('oyun', '')
    kateqori = request.args.get('kateqori', '')
    fikr = request.args.get('fikr', '')

    return render_template_string(html, mesaj=mesaj, ad=ad, oyun=oyun, kateqori=kateqori, fikr=fikr, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
