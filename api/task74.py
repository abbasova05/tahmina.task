from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)
CSV_FILE = 'oyunlar.csv'

html = '''
<!DOCTYPE html>
<html>
<head>
    <title> Oyun fikirleri</title>
</head>
<body>
    <h2> Seviyiniz oyunu yazin </h2>
    <form method="POST">
        <label>Adiniz:</label><br>
        <input type="text" name="ad" required><br><br>

        <label>Oyun adi:</label><br>
        <input type="text" name="oyun" required><br><br>

        <label> Oyunun kateqorisi: </label><br><br>
        <input type="text" name="kateqori" required><br><br>

        <label> Bu oyunu niye tovsiye edirsiniz </label><br>
        <textarea name="fikr" rows="5" cols="40" placeholder="Buraya sebebini yazin..." required></textarea><br><br>

        <input type="submit" value="Gonder">
    </form>

    {% if mesaj %}
        <hr>
        <h3 style="color:green;">{{ mesaj }}</h3>
        <p><strong>Ad:</strong> {{ ad }}</p>
        <p><strong>Oyun:</strong> {{ oyun }}</p>
        <p><strong>Kateqori:</strong> {{ kateqori }}</p>
        <p><strong>Fikrin:</strong> {{ fikr }}</p>
    {% endif %}
</body>
</html>    
'''

def yaz_oyun(ad, oyun, kateqori, fikr):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([ad, oyun, kateqori, fikr])

@app.route('/', methods=['GET', 'POST'])
def index():
    mesaj = ''
    ad = oyun = kateqori = fikr = ''
    if request.method == 'POST':
        ad = request.form.get('ad')
        oyun = request.form.get('oyun')
        kateqori = request.form.get('kateqori')
        fikr = request.form.get('fikr')
        yaz_oyun(ad, oyun, kateqori, fikr)
        mesaj = "Tofsiyyeniz qeyd edildiiiii"
    return render_template_string(html, mesaj=mesaj, ad=ad, oyun=oyun, kateqori=kateqori, fikr=fikr)

@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    ad = data.get('ad')
    oyun = data.get('oyun')
    kateqori = data.get('kateqori')
    fikr = data.get('fikr')
    yaz_oyun(ad, oyun, kateqori, fikr)
    return {'mesaj': 'Melumat PUT metotu ile alindi ve qey edildi.'}, 200

@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    ad = data.get('ad')
    oyun = data.get('oyun')
    kateqori = data.get('kateqori')
    
    if not ad or not oyun or not kateqori:
        return {'xeta': 'Ad, oyun, ve kateqoriya teleb olunur.'}, 400
    
    lines = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        lines = [row for row in reader if not (row[0] == ad and row[1] == oyun and row[2] == kateqori)]

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(lines)

    return {'mesaj': 'verilen oyun fikiri silindi'}, 200

if __name__ =='__main__':
    app.run(debug=True)        



