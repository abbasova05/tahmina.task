from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_average():
    message = ''
    if request.method == 'POST':
        data = request.form.get('data', '')
        try:
            numbers = [float(x.strip()) for x in data.split(',')]
            average = sum(numbers) / len(numbers)
            message = f"Verilən ədədlərin orta qiyməti: {average:.3f}"
        except ValueError:
            message = "Xahiş olunur, ədədləri düzgün formatda, vergüllə ayrılmış şəkildə daxil edin."
    return render_template_string('''
        <h2>Ortalama Hesablama</h2>
        <form method="POST">
            Ədədləri vergüllə ayıraraq daxil edin:<br>
            <input type="text" name="data" style="width:300px;" required>
            <button type="submit">Hesabla</button>
        </form>
        <div style="margin-top:20px; font-weight:bold; color:blue;">
            {{ message }}
        </div>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)
