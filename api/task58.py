from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def survey():
    answer = ''
    if request.method == 'POST':
        answer = request.form.get('color', '')
        if answer:
            answer = f"Sizin seçdiyiniz rəng: {answer}"
        else:
            answer = "Zəhmət olmasa rəng seçin."
    return render_template_string('''
        <h2>Sevdiyiniz rəngi seçin</h2>
        <form method="POST">
            <input type="radio" name="color" value="Qırmızı"> Qırmızı<br>
            <input type="radio" name="color" value="Mavi"> Mavi<br>
            <input type="radio" name="color" value="Yaşıl"> Yaşıl<br>
            <input type="radio" name="color" value="Sarı"> Sarı<br>
            <input type="submit" value="Göndər">
        </form>
        <p>{{ answer }}</p>
    ''', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
