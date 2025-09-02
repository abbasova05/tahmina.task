from flask import Flask, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1 style="text-align: center;">Sade blog sistemi</h1>
    <a href= "/blog">Bloga kec</a>
'''

@app.route("/blog", methods=["GET", "POST"])
def blog():
    mesaj = ""
    if request.method == "POST":
        basliq = request.form["basliq"].strip()
        metn = request.form["metn"].strip()

        if basliq and metn:
            with open("blog.csv", "a", newline='', encoding="utf-8") as f:
                csv.writer(f).writerow([basliq, metn])
            mesaj = "Post uğurla əlavə edildi!"
        else:
            mesaj = "Boş buraxmayın!"
            
    try:
        with open("blog.csv", newline='', encoding="utf-8") as f:
            postlar = list(csv.reader(f))
    except FileNotFoundError:
        postlar = []


    html = f'''
    <h2>Sadə Blog Sistemi</h2>
    <form method="POST">
        Başlıq: <input name="basliq"><br><br>
        Mətn: <br><textarea name="metn" rows="5" cols="40"></textarea><br><br>
        <input type="submit" value="Paylaş">
    </form>
    <p style="color:green;">{mesaj}</p>
    <hr>
    <h3>Əvvəlki Paylaşımlar:</h3>
    '''

    for basliq, metn in reversed(postlar): 
        html += f"<b>{basliq}</b><br>{metn}<hr>"

    return html

if __name__ == "__main__":
    app.run(port=1453, debug=True, host="")