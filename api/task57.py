from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def reverse_text():
    result = ''
    if request.method == 'POST':
        text = request.form.get('text', '')
        result = text[::-1]
    return render_template_string('''
        <form method="POST">
            Mətn daxil edin:<br>
            <input name="text" style="width:300px;" required>
            <input type="submit" value="Ters çevir">
        </form>
        <p><b>Nəticə:</b> {{ result }}</p>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
