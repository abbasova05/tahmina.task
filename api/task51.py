from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    background_color = "#FFFFFF"  
    if request.method == "POST":
        selected_color = request.form.get("color")
        if selected_color:
            background_color = selected_color
    return render_template("color.html", background=background_color)

if __name__ == "__main__":
    app.run(debug=True)
