from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            result = num1 + num2
        except ValueError:
            result = "Zəhmət olmasa düzgün ədədlər daxil edin."
    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
