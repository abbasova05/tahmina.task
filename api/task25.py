from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route("/")
def home():
    return 'Hello World'

@app.route("/about")
def about():
    return 'The about page'

@app.route("/blog")
def blog():
    posts = [{'title': 'Tecnology in 2019', 'author': 'Avi'},
        {'title': 'Expansion of oil', 'author': 'bob'}]
    return render_template("blog.html" , author = "Bob", sunny=False, posts=posts)

@app.route("/blog/<string:blog_id>")
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id

@app.route("/contact")
def contact():
    return "This is the contact page"

@app.route("/user/<string:username>")
def user_profile(username):
    return f"Welcome to {username}'s profile!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1454)