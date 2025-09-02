from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def max_number():
    result = ''
    if request.method == 'POST':
        try:
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            maximum = max(a, b)
            result = f"Böyük ədəd: {maximum}"
        except:
            result = "Zəhmət olmasa düzgün ədədlər daxil edin."
    return render_template_string('''
        <form method="POST">
            1-ci ədəd: <input name="a" required><br>
            2-ci ədəd: <input name="b" required><br>
            <input type="submit" value="Tap">
        </form>
        <p>{{ result }}</p>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
