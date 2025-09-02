from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("oyun.html")

if __name__ == "__main":
    app.run(port=1453, debug=True)