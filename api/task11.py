from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def home():
    return '''
    <h1>GET metodu</h2>
    <form method="POST">
    AD: <input type="text" name="ad">
    <input type="submit" value="POST ile gonder">
    </form>
    <form method="POST" action="/?method=PUT">
    Yeni ad; <input type="text" name="ad">
    <input type="submit" value="PUT ile yenile">
    </form>
    <form method="POST" action=/?method=DELETE>
    <input type="submit" value="DELTE ILE SIL>
    </form>
    '''

def post():
    ad = request.form.get("ad")
    return f"salam, {ad}!"

def put():
    ad = request.form.get("ad")
    return f"ad yenilendi: {ad}"

def delete():
    return "melumat silindi"



if __name__ == "__main__":
    app.run(port=5025)