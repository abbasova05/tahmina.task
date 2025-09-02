from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1 style="text-align: center; ">ilkkkkkk  baxisssss</h1>

    <a href ="/esas">esaslarr!</a><br>
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
            return f"Salammmm {ad} {soyad}"
        else:
            return "Melumat yoxdurrrrrrrrrrr!!!!!!!"    
    else:
        return '''
    <h1 style="text-align: cenetr;">nese elemeye calisiriq</h1>
    <form method="POST">
    AD: <input type="text" name="ad"><br>
    <br>
    SOYAD: <input type="text" name="soyad"><br>
    <br>
    <input type="submit" value="gonder"><br>
    </form>
    '''    

@app.route("/elave", methods=["GET", "POST"])
def elave     

if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0",port=1453)


    
    