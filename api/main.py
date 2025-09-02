from flask import Flask
import mdice

app = Flask(__name__)

@app.route('/')
def start():
    return '''
<h2>KODY>AZ & FLASK<br>
<a href='/about'>About page</a>
'''

@app.route('/about')
def about():
    return f'''
<h2>ABOUT FLASK {mdice.show_dice()}</h2>
<a href='/'>Main page</a>
'''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)