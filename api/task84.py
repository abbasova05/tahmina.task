from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# SQLite məlumat bazasının fayl yolu (hazırda layihə qovluğunda "todo.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Məlumat bazasında saxlanacaq model (cədvəl)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
# Məlumat bazasını yaradın (ilk dəfə işlədərkən)
@app.before_first_request
def create_tables():
    db.create_all()
# Bütün tapşırıqları əldə etmək
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])
# Yeni tapşırıq əlavə etmək
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or not 'title' in data:
        return jsonify({'error': 'Task title is required'}), 400
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201
# Tapşırığı yeniləmək (başlıq və ya tamamlanma vəziyyəti)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json()
    if 'title' in data:
        task.title = data['title']
    if 'completed' in data:
        task.completed = data['completed']
    db.session.commit()
    return jsonify(task.to_dict())
# Tapşırığı silmək
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})
# Serveri işə salmaq
if __name__ == '__main__':
    app.run(debug=True)