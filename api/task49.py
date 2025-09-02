from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def pick_month():
    selected_month = None
    if request.method == "POST":
        selected_month = request.form.get("month")
    return render_template("month_picker.html", selected_month=selected_month)

if __name__ == "__main__":
    app.run(debug=True)
