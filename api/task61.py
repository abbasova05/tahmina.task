from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string('''
        <h2>Server vaxtı:</h2>
        <p>{{ time }}</p>
    ''', time=now)

if __name__ == '__main__':
    app.run(debug=True)
