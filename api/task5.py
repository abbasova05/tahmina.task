from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <strong>Flask</strong><br>
    <small>RestfulApi</small><br>
    <ins>Tahmina</ins><br>
    """

if __name__ == ("__main__"):
    app.run(port=5018)