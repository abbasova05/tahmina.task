from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("render.html")

@app.route("/Aboutt")
def aboutt():
        return render_template("aboutt.html")

@app.route("/comment", methods=["GET", "POST", "PUT"])
def comment():
    comment_data = {}
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        username = request.form.get("username", "")
        comment = request.form.get("comment", "")
        comment_data["username"] = username
        comment_data["comment"] = comment
        return render_template("result.html", username=username, comment=comment)
    elif request.method == "PUT":
        username = request.json.get("username", "")
        comment = request.json.get("comment", "")
        comment_data["username"] = username
        comment_data["comment"] = comment
        return render_template("result.html", username=username, comment=comment)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)