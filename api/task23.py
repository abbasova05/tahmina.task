from flask import Flask, request, jsonify
import json

app = Flask(__name__)
DATA_FILE = 'todo.json'

def read_tasks():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/todo-list', methods=['GET'])
def get_all_tasks():
    tasks = read_tasks()
    return jsonify(tasks)

@app.route('/todo-list', methods=['POST'])
def add_task():
    new_task = request.json  
    if not isinstance(new_task, dict) or len(new_task) != 1:
        return jsonify({"error": "Please provide a dictionary with a single key-value pair"}), 400

    tasks = read_tasks()

    new_key = list(new_task.keys())[0]
    for task in tasks:
        if new_key in task:
            return jsonify({"error": "Key already exists"}), 400

    tasks.append(new_task)
    write_tasks(tasks)
    return jsonify({"message": "Task added", "task": new_task}), 201

@app.route('/todo-list/<string:key>', methods=['PUT'])
def update_task(key):
    updated_value = request.json.get("value")
    if not updated_value:
        return jsonify({"error": "Please provide 'value' in json body"}), 400

    tasks = read_tasks()
    for task in tasks:
        if key in task:
            task[key] = updated_value
            write_tasks(tasks)
            return jsonify({"message": "Task updated", "task": task})

    return jsonify({"error": "Key not found"}), 404

@app.route('/todo-list/<string:key>', methods=['DELETE'])
def delete_task(key):
    tasks = read_tasks()
    for i, task in enumerate(tasks):
        if key in task:
            deleted_task = tasks.pop(i)
            write_tasks(tasks)
            return jsonify({"message": "Task deleted", "task": deleted_task})

    return jsonify({"error": "Key not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
