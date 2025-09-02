from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ad = request.form.get("ad")
        return f"Salam, {ad}!"
    else:
        return '''
        <form method="POST">
        Adiniz: <input type="text" name="ad">
        <input type="submit" value="Göndər">
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=1453)  