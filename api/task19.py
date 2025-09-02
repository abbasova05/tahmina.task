from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1 style="text-align: center;">ilkkkkkk  baxisssss</h1>
    <a href="/esas">esaslarr!</a><br>
    <a href="/elave">sistemm!</a><br>
    <a href="/komekci">digerleri!</a><br>
    <a href="/diger">bosss!</a><br>
    '''
@app.route("/esas", methods=["GET", "POST"])
def esas():
    if request.method == "POST":
        ad = request.form.get("ad")
        soyad = request.form.get("soyad")
        if ad:
            return f"<h2>Salammmm {ad} {soyad}</h2>"
        else:
            return "<h2>Melumat yoxdurrrrrrrrrrr!!!!!!!</h2>"
    else:
        return '''
        <h1 style="text-align: center;">nese elemeye calisiriq</h1>
        <form method="POST">
            AD: <input type="text" name="ad"><br><br>
            SOYAD: <input type="text" name="soyad"><br><br>
            <input type="submit" value="gonder"><br>
        </form>
        '''
@app.route("/elave", methods=["GET", "POST"])
def elave():
    if request.method == "POST":
        email = request.form.get("email")
        tel = request.form.get("tel")
        if email and tel:
            return f'''<h2>Email: {email}<br>
            Telefon: {tel}</h2>'''
        else:
            return "<h2>Email və ya telefon daxil edilməyib!</h2>"
    else:
        return '''
        <h1 style="text-align: center;">Əlavə Məlumat</h1>
        <form method="POST">
            Email: <input type="email" name="email"><br><br>
            Telefon: <input type="text" name="tel"><br><br>
        
            <input type="submit" value="Göndər"><br>
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1454)