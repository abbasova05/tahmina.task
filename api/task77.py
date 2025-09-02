from flask import Flask, request, redirect, url_for
app = Flask(__name__)
tasks = []
@app.route("/", methods=["GET", "POST"])
def index():
    global tasks
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append({"task": task, "done": False})
        return redirect(url_for("index"))
    tasks_html = ""
    for i, t in enumerate(tasks):
        status = ":heavy_check_mark:" if t["done"] else ":x:"
        tasks_html += f"""
        <li>
            {t['task']} — Status: {status}
            <a href="/done/{i}">Tamamla</a> |
            <a href="/delete/{i}">Sil</a>
        </li>
        """
    return f"""
    <h1>Gundelik Planlayici</h1>
    <form method="POST">
        Tapsiriq elave et: <input type="text" name="task" required>
        <button type="submit">Elavə et</button>
    </form>
    <ul>
        {tasks_html if tasks else '<li>Hec bir tapsiriq yoxdur.</li>'}
    </ul>
    """
@app.route("/done/<int:task_id>")
def done(task_id):
    global tasks
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
    return redirect(url_for("index"))
@app.route("/delete/<int:task_id>")
def delete(task_id):
    global tasks
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)