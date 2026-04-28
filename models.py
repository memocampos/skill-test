from typing import Dict

class TaskStore:
    def __init__(self):
        self.tasks: Dict[int, dict] = {}
        self.counter = 1

    def get_all(self):

        return list(self.tasks.values())

    def get(self, task_id: int):
        return self.tasks.get(task_id)

    def create(self, title: str, description: str):
        task = {
            "id": self.counter,
            "title": title,
            "description": description
        }
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def update(self, task_id: int, title: str, description: str):
        if task_id not in self.tasks:
            return None

        self.tasks[task_id].update({
            "title": title,
            "description": description
        })
        return self.tasks[task_id]

    def delete(self, task_id: int):
        return self.tasks.pop(task_id, None)


store = TaskStore()