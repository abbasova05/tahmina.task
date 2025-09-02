from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def checkbox_survey():
    selected = []
    if request.method == 'POST':
        selected = request.form.getlist('hobbies')
    return render_template_string('''
        <form method="POST">
            Sevdiyiniz məşğuliyyətləri seçin:<br>
            <input type="checkbox" name="hobbies" value="Oxumaq"> Oxumaq<br>
            <input type="checkbox" name="hobbies" value="İdman"> İdman<br>
            <input type="checkbox" name="hobbies" value="Səyahət"> Səyahət<br>
            <input type="checkbox" name="hobbies" value="Musiqi"> Musiqi<br>
            <input type="submit" value="Göndər">
        </form>
        <p>Seçilənlər: {{ selected }}</p>
    ''', selected=selected)

if __name__ == '__main__':
    app.run(debug=True)
