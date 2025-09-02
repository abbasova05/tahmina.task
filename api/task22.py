from flask import Flask, jsonify, request, abort

app = Flask(__name__)

tasks = [
    {'id': 1, 'task': 'Kitab oxu'},
    {'id': 2, 'task': 'Kod yaz'}
]

@app.route('/tasks/', methods=['GET'])
def get_tasks():
    """Bütün task-ları qaytarır"""
    return jsonify(tasks)

@app.route('/tasks/', methods=['POST'])
def add_task():
    """Yeni task əlavə edir"""
    if not request.json or 'task' not in request.json:
        abort(400, description="Task məzmunu göndərilməlidir")

    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'task': request.json['task']
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    """Verilmiş ID ilə task qaytarır"""
    task = next((t for t in tasks if t['id'] == id), None)
    if task is None:
        return jsonify({'message': 'Tapılmadı'}), 404
    return jsonify(task)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """Mövcud task-ı yeniləyir"""
    task = next((t for t in tasks if t['id'] == id), None)
    if task is None:
        return jsonify({'message': 'Tapılmadı'}), 404

    if not request.json or 'task' not in request.json:
        abort(400, description="Task məzmunu göndərilməlidir")

    task['task'] = request.json['task']
    return jsonify(task)

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """Task-ı silir"""
    global tasks
    task = next((t for t in tasks if t['id'] == id), None)
    if task is None:
        return jsonify({'message': 'Tapılmadı'}), 404

    tasks = [t for t in tasks if t['id'] != id]
    return jsonify({'message': f'Task {id} silindi'})

if __name__ == '__main__':
    app.run(debug=True)
