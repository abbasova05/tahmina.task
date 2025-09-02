
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """
    <h1 style="color:purple;">Salam</h1>
    <h2 style="color:red;">hellooooooooo</h2>
    <h3 style="color:yellow;">Tahmina</h3>
    <h4 style="color:orange;">necesiz</h4>
    <h5 style="color:grey;">flaskk</h5>
    <h6 style="color:brown;">restfull</h6>
    <p style="color:blue;">Men Tehmine</p>
    """

if __name__ == "__main__":
    app.run(port=5011)

    return '<h1>Flask REST API</h1>'

if __name__=="__main__":
    app.run(debug=True)
