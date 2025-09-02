from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            operation = request.form.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    error = "Sıfıra bölmək olmaz!"
                else:
                    result = num1 / num2
            else:
                error = "Əməliyyat seçilməyib."
        except ValueError:
            error = "Zəhmət olmasa düzgün ədədlər daxil edin."

    return render_template("calculatorr.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
