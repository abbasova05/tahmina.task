from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("render.html")

@app.route("/Aboutt")
def aboutt():
        return render_template("aboutt.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)