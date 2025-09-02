from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='My API',
          description='Sadə Swagger API sənədləşdirmə nümunəsi')

ns = api.namespace('tasks', description='Task əməliyyatları')

tasks = [
    {'id': 1, 'task': 'Kitab oxu'},
    {'id': 2, 'task': 'Kod yaz'},
    {'id': 3, 'task': 'Tahmina'}
]

@ns.route('/')
class TaskList(Resource):
    def get(self):
        """Bütün task-ları qaytarır"""
        return tasks

    def post(self):
        """Yeni task əlavə edir"""
        new_task = {'id': len(tasks) + 1, 'task': 'Yeni task'}
        tasks.append(new_task)
        return new_task, 201

@ns.route('/<int:id>')
class Task(Resource):
    def get(self, id):
        """Verilmiş ID ilə task qaytarır"""
        for task in tasks:
            if task['id'] == id:
                return task
        return {'message': 'Tapılmadı'}, 404

if __name__ == '__main__':
    app.run(debug=True)
