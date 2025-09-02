from flask import Flask, request, jsonify, render_template_string
import csv

app = Flask(__name__)
CSV_FILE = 'oyunlar.csv'

html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Oyun fikirleri</title>
</head>
<body>
    <h2>Oyun fikirlerini gosterir</h2>
    <ul>
    {% for o in oyunlar %}
        <li><strong>{{ o[1] }}</strong> ({{ o[2] }}) - {{ o[3] }} <em>by {{ o[0] }}</em></li>
    {% else %}
        <li>Heç bir fikir yoxdur.</li>
    {% endfor %}
    </ul>
</body>
</html>
'''

def read_oyunlar():
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        return []

def write_oyunlar(oyunlar):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(oyunlar)

@app.route('/oyunlar', methods=['POST'])
def add_oyun():
    data = request.get_json()
    ad = data.get('ad')
    oyun = data.get('oyun')
    kateqori = data.get('kateqori')
    fikr = data.get('fikr')

    if not all([ad, oyun, kateqori, fikr]):
        return jsonify({'error': 'Bütün sahələr tələb olunur'}), 400

    oyunlar = read_oyunlar()

    changed = False
    for i, row in enumerate(oyunlar):
        if row[0] == ad and row[1] == oyun and row[2] == kateqori:
            oyunlar[i] = [ad, oyun, kateqori, fikr]
            changed = True
            break
    if not changed:
        oyunlar.append([ad, oyun, kateqori, fikr])

    write_oyunlar(oyunlar)
    return jsonify({'message': 'Oyun fikri əlavə edildi və ya yeniləndi'}), 201

@app.route('/oyunlar', methods=['GET'])
def get_oyunlar():
    oyunlar = read_oyunlar()
    return jsonify(oyunlar), 200

@app.route('/oyunlar/<ad>/<oyun>/<kateqori>', methods=['DELETE'])
def delete_oyun(ad, oyun, kateqori):
    oyunlar = read_oyunlar()
    original_len = len(oyunlar)
    oyunlar = [row for row in oyunlar if not (row[0]==ad and row[1]==oyun and row[2]==kateqori)]
    if len(oyunlar) == original_len:
        return jsonify({'error': 'Fikir tapılmadı'}), 404
    write_oyunlar(oyunlar)
    return jsonify({'message': 'Fikir silindi'}), 200

@app.route('/oyunlar/view')
def view_oyunlar():
    oyunlar = read_oyunlar()
    return render_template_string(html_template, oyunlar=oyunlar)

if __name__ == '__main__':
    app.run(debug=True)
