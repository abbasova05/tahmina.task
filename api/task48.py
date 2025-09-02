from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Salam, Xoş Gəlmisiniz!"

@app.route("/services")
def services():
    return "Bizim xidmətlər səhifəmiz"

@app.route("/products")
def products():
    product_list = [
        {"id": 1, "name": "Telefon", "price": 500},
        {"id": 2, "name": "Komputer", "price": 1200},
        {"id": 3, "name": "Planşet", "price": 300}
    ]
    return render_template("products.html", products=product_list)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    return f"Məhsulun ID-si: {product_id}"

@app.route("/profile/<string:username>")
def profile(username):
    return f"Salam, {username}! Profil səhifənə xoş gəlmisən."

if __name__ == "__main__":
    app.run(debug=True)
