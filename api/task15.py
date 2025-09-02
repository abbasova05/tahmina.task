from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style="text-align: center;">Ilk baxissss</h1>
    <a href="/elave">sistemmmmm</a><br>
    """

@app.route("/elave", methods=["GET", "POST"])
def elave():
    if request.method == "POST":
        ad = request.form.get("ad")
        yeniad = request.form.get("yeniad")
        if ad :
            return f"Salam, {ad}!"
        elif yeniad:
            return f"salammmmm, {yeniad}!"
        else:
            return "Melumat gosderilmiyib"
    else:
        return '''
        <h1 style="text-align: center;">Sade sistem</h1>
        <form method="POST">
        Adiniz: <input type="text" name="ad">
        <input type="submit" value="Göndər">
        </form>
        <form method="POST">
        Yeni adiniz: <input type="text" name="yeniad">
        <input type="submit" value="gonder">
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=1453)   