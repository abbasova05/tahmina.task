from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route("/")
def home():
    return 'Hello World'

@app.route("/about")
def about():
    return render_template("info.html", name="Codex", year=2025)

@app.route("/blog")
def blog():
    posts = [{'title': 'Tecnology in 2019', 'author': 'Avi'},
             {'title': 'Expansion of oil', 'author': 'bob'}]
    return render_template("blog.html", author="Bob", sunny=False, posts=posts)

@app.route("/blog/<string:blog_id>")
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1454)
