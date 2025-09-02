from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Ana səhifə</h1><p>Salam, xoş gəlmisən!</p>"

@app.route("/haqqimda")
def haqqinda():
    return "<h1>Haqqımda</h1><p>Mən Tahminayam, Flask öyrənirəm.</p>"

@app.route("/elaqe")
def elaqe():
    return "<h1>Əlaqə</h1><p>Email: tahmina@example.com</p>"

if __name__ == "__main__":
    app.run(port=5013)