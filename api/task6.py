from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"""
    <h1>Basliqqqqqq</h1><br>
    <a href="/haqqinda">melumatttt</a><br>
    <a href="/esaslarr">diger</a><br>
    <a href="/tapsiriqlar">task</a><br>
    <a href="/https://example.com" target=_blank">Xarici sayt</a><br>
    """

if __name__==("__main__"):
    app.run(port=5020)