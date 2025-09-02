from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Əlaqə formu</title>
</head>
<body>
    <h2>Əlaqə məlumatlarını daxil edin</h2>
    <form method="POST">
        <label>Ad:</label>
        <input type="text" name="ad" required><br><br>

        <label>Telefon nömrəsi:</label>
        <input type="tel" name="telefon" placeholder="+994 XX XXX XX XX" pattern="[+0-9\s\-]+" required><br><br>

        <label>Əlavə məlumat:</label><br>
        <textarea name="melumat" rows="4" cols="40" placeholder="Buraya əlavə məlumat yaza bilərsiniz..."></textarea><br><br>

        <input type="submit" value="Göndər">
    </form>

    {% if ad and telefon %}
        <h3>Daxil etdiyiniz məlumatlar:</h3>
        <p><strong>Ad:</strong> {{ ad }}</p>
        <p><strong>Telefon:</strong> {{ telefon }}</p>
        {% if melumat %}
            <p><strong>Əlavə məlumat:</strong> {{ melumat }}</p>
        {% endif %}
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    ad = telefon = melumat = None
    if request.method == 'POST':
        ad = request.form.get('ad')
        telefon = request.form.get('telefon')
        melumat = request.form.get('melumat')
    return render_template_string(html, ad=ad, telefon=telefon, melumat=melumat)

if __name__ == '__main__':
    app.run(debug=True)
