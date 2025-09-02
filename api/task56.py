from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def average():
    result = ''
    if request.method == 'POST':
        numbers = request.form.get('numbers', '')
        try:
            nums = [float(n) for n in numbers.split(',')]
            avg = sum(nums) / len(nums)
            result = f"Ədədlərin ortalaması: {avg:.2f}"
        except:
            result = "Zəhmət olmasa ədədləri vergüllə ayrılmış formada daxil edin."
    return render_template_string('''
        <form method="POST">
            Ədədləri vergüllə ayrılmış şəkildə daxil edin:<br>
            <input name="numbers" style="width:300px;" required>
            <input type="submit" value="Hesabla">
        </form>
        <p>{{ result }}</p>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
