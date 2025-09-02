from flask import Flask, render_template

app = Flask(__name__)

# Məhsul məlumatları (ad, şəkil, link)
products = [
    {
        "name": "Alma",
        "image": "alma.jpg",
        "link": "https://example.com/alma"
    },
    {
        "name": "Armud",
        "image": "armud.jpg",
        "link": "https://example.com/armud"
    },
    {
        "name": "Banana",
        "image": "banan.jpg",
        "link": "https://example.com/banana"
    },
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1454)