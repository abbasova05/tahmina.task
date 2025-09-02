from flask import Flask

app = Flask(__name__)

@app.route("/")
def sekil():
    return """
    <h2>Bu mənim şəkilimdir</h2>
    <img src="https://via.placeholder.com/150" alt="sekil">
    """

if __name__ =="__main__":
    app.run(port=5008)
