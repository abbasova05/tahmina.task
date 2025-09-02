from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def count_words():
    word_count = None
    error = None
    text = ""
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            words = text.split()
            word_count = len(words)
        else:
            error = "Zəhmət olmasa mətn daxil edin."
    return render_template("count_words.html", word_count=word_count, error=error, text=text)

if __name__ == "__main__":
    app.run(debug=True)
