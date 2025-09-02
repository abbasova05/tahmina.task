from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {'id': 1, 'task': 'Kitab oxu'},
    {'id': 2, 'task': 'Kod yaz'},
    {'id': 3, 'task': 'Tahmina'},
]

@app.route('/tasks', methods=['GET'])
def show_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json.get('task')
    if not new_task:
        return {"error": "Task metnini gönderin"}, 400
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    task = {'id': new_id, 'task': new_task}
    tasks.append(task)
    return jsonify(task), 201


if __name__ == '__main__':
    app.run(debug=True)