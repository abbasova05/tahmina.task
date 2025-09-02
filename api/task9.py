from flask import Flask, request

app = Flask(__name__)

@app.route("/melumat", methods = ["GET", "POST", "PUT", "DELETE"])
def melumat():
    if request.method == "GET":
        return "GET: Melumat gosderildi. "
    
    elif request.method == "POST":
        return "POST: Yenimelumat elave olundu. "
    
    elif request.method == "PUT":
        return "PUT: Melumat deyisdirildi. "
    
    elif request.method == "DELETE":
        return "DELETE: Melumat silindi. "
    
    else:
        return "Metot desteklenmir 404 "
    
if __name__ == "__main__ ":
    app.run(port=5076)