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
            mesaj = "✅ Post uğurla əlavə edildi!"
        else:
            mesaj = "⚠️ Zəhmət olmasa bütün xanaları doldurun!"

    # CSV faylından yazıları oxu
    try:
        with open("blog.csv", newline='', encoding="utf-8") as f:
            postlar = list(csv.reader(f))
    except FileNotFoundError:
        postlar = []

    # HTML ilə cavab
    html = f'''
    <html>
    <head>
        <title>Sadə Blog</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                text-align: center;
            }}
            h2 {{
                color: #333;
            }}
            form {{
                margin: 20px auto;
                width: 50%;
                background: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: left;
            }}
            input[type="text"], textarea {{
                width: 100%;
                padding: 10px;
                margin-top: 5px;
                border-radius: 4px;
                border: 1px solid #ccc;
            }}
            input[type="submit"] {{
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                margin-top: 10px;
            }}
            .mesaj {{
                color: green;
                font-weight: bold;
                margin-top: 15px;
            }}
            .post {{
                background-color: #ffffff;
                margin: 20px auto;
                width: 50%;
                padding: 15px;
                border-radius: 6px;
                box-shadow: 0 0 5px rgba(0,0,0,0.1);
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <h2>Sadə Blog Sistemi</h2>

        <form method="POST">
            <label><b>Başlıq:</b></label><br>
            <input name="basliq" type="text"><br><br>

            <label><b>Mətn:</b></label><br>
            <textarea name="metn" rows="5" cols="40"></textarea><br><br>

            <input type="submit" value="Paylaş">
        </form>

        <div class="mesaj">{mesaj}</div>
        <hr>
        <h3>Əvvəlki Paylaşımlar:</h3>
    '''

    for basliq, metn in reversed(postlar):
        html += f'''
        <div class="post">
            <b>{basliq}</b><br>
            <p>{metn}</p>
        </div>
        '''

    html += "</body></html>"
    return html

if __name__ == "__main__":
    app.run(port=1453, debug=True, host="")