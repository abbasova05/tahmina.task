from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1> Esas sehife</h1>
    <a href="/esas_melumat">melumat</a><br>
    <a href="/digermelumatlar">elave</a><br>
    '''

@app.route("/esas_melumat", method =["GET","POST"])
def melumat():
    melumat = ""
    if request.method == "GET":
        return


