from flask import Flask, request, render_template
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/notes", methods=["GET", "POST"])
def notes():
    mesaj = ""
    if request.method == "POST":
        ad = request.form.get("ad", "").strip()
        qeyd = request.form.get("qeyd", "").strip()

        if ad and qeyd:
            vaxt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("notes.csv", "a", newline='', encoding="utf-8") as f:
                csv.writer(f).writerow([ad, qeyd, vaxt])
            mesaj = "Qeyd uğurla əlavə edildi!"
        else:
            mesaj = "Ad və qeyd boş ola bilməz!"

    try:
        with open("notes.csv", newline='', encoding="utf-8") as f:
            butun_qeydlər = list(csv.reader(f))
    except FileNotFoundError:
        butun_qeydlər = []

    return render_template("notes.html", mesaj=mesaj, qeydlər=reversed(butun_qeydlər))

if __name__ == "__main__":
    app.run(port=1453, debug=True)
