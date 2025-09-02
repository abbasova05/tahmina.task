from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def square():
    result = ""
    if request.method == "POST":
        try:
            num = int(request.form.get("number", "0"))
            result = f"{num}² = {num*num}"
        except ValueError:
            result = "Zəhmət olmasa düzgün rəqəm daxil edin."
    return render_template("hesablama.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
