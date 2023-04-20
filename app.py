from flask import Flask, jsonify, request, abort
from datetime import datetime
from dateutil.parser import parse

app = Flask(__name__)

tasks = []
task_id_counter = 1


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


def find_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None


def validate_task_data(task_data):
    if not task_data or 'title' not in task_data:
        return False
    return True

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    task_data = request.get_json()

    if not validate_task_data(task_data):
        abort(400)

    task = {
        'id': task_id_counter,
        'title': task_data['title'],
        'description': task_data.get('description', ''),
        'due_date': parse(task_data['due_date']) if 'due_date' in task_data else None,
        'completed': False
    }
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = find_task(task_id)
    if task is None:
        abort(404)

    task_data = request.get_json()
    if not validate_task_data(task_data):
        abort(400)

    task['title'] = task_data['title']
    task['description'] = task_data.get('description', task['description'])
    task['due_date'] = parse(task_data['due_date']) if task_data.get('due_date') else task['due_date']
    task['completed'] = task_data.get('completed', task.get('completed', False))  # Update this line

    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task(task_id)
    if task is None:
        abort(404)
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = find_task(task_id)
    if task is None:
        abort(404)

    tasks.remove(task)
    return '', 204


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
