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
@app.route("/haqqinda")
def haqqinda():
    return"""
    <h2>Haqqımda</h2><br>
    <p>Salam,Tahmina</p><br>
    <a href="/">geri qayit</a><br>
    """
@app.route("/esaslarr")
def esaslarr():
    return"""
    <strong>emailllllll</strong>
    """

if __name__==("__main__"):
    app.run(port=5021)