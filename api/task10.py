from flask import Flask, request

add = Flask(__name__)

@add.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def home():
    method = request.method
    if method == "GET":
        return "GET: Ana sehife acildi. "
    elif method == "POST":
        return "POST: Yeni melumat. "
    elif method == "PUT":
        return "PUT: Melumat elave olundu. "
    elif method == "DELETE":
        return "DELETE: Melumat silindi. "
    else:
        return "Xeta. "

if __name__ == "__main__":
    add.run(port=5024)        
    
