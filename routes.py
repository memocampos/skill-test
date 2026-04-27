from flask import Blueprint, request, jsonify, render_template
from models import store

task_bp = Blueprint("tasks", __name__)


def validate_payload(data):
    if not data:
        return "Request body is required"

    if "title" not in data or "description" not in data:
        return "Missing required fields: title, description"

    if not data["title"].strip():
        return "Title cannot be empty"

    return None


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(store.get_all()), 200


@task_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = store.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200


@task_bp.route("/tasks", methods=["POST"])
def create_task():
    print("POST /New task")
    data = request.get_json()
    error = validate_payload(data)

    if error:
        return jsonify({"error": error}), 400

    task = store.create(data["title"], data["description"])
    return jsonify(task), 201


@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    print("PUT Updating task", task_id)
    data = request.get_json()
    error = validate_payload(data)

    if error:
        return jsonify({"error": error}), 400

    task = store.update(task_id, data["title"], data["description"])
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    print("/tasks/<int:task_id>", task_id)
    task = store.delete(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return "", 204


@task_bp.route("/", methods=["GET"])
def home():
    print("/ GET")
    tasks = store.get_all()
    return render_template("tasks.html", tasks=tasks)