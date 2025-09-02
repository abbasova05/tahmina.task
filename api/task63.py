from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def display_current_time():
    now = datetime.now()
    formatted_time = now.strftime("%A, %d %B %Y — %H:%M:%S")
    return render_template_string('''
        <html>
        <head>
            <title>Server Vaxtı</title>
            <meta http-equiv="refresh" content="5">
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    color: #333;
                    text-align: center;
                    padding-top: 50px;
                }
                h1 {
                    color: #007acc;
                }
                p {
                    font-size: 1.5em;
                    font-weight: bold;
                }
                small {
                    color: #666;
                }
            </style>
        </head>
        <body>
            <h1>İndiki Server Vaxtı</h1>
            <p>{{ time }}</p>
            <small>Səhifə hər 5 saniyədən bir avtomatik yenilənir.</small>
        </body>
        </html>
    ''', time=formatted_time)

if __name__ == '__main__':
    app.run(debug=True)
