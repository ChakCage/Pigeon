class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return f"{self.id}: {self.title} - {self.completed}"


class TaskNotFoundError(Exception):
    pass


class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        new_id = len(self.tasks) + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.complete()
                return task

        raise TaskNotFoundError

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return

        raise TaskNotFoundError