from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Telefon nömrəsi formu</title>
</head>
<body>
    <h2>Telefon nömrəsi daxil edin</h2>
    <form method="POST">
        <label>Telefon nömrəsi:</label>
        <input type="tel" name="telefon" placeholder="+994 XX XXX XX XX" pattern="[+0-9\s\-]+" required>
        <input type="submit" value="Göndər">
    </form>
    {% if telefon %}
        <p>Girdiyiniz telefon nömrəsi: <strong>{{ telefon }}</strong></p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    telefon = None
    if request.method == 'POST':
        telefon = request.form.get('telefon')
    return render_template_string(html, telefon=telefon)

if __name__ == '__main__':
    app.run(debug=True)
