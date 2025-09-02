from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    selected_options = []
    if request.method == "POST":
        selected_options = request.form.getlist("colors")
    return render_template("reng.html", selected=selected_options)

if __name__ == "__main__":
    app.run(debug=True)
