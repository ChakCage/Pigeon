from core.task_repository import TaskRepository


class Task:
    def __init__(self, id, title, description, is_completed, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = is_completed
        self.created_at = created_at

    def __str__(self):
        return f"{self.id}: {self.title} - {self.is_completed}"


class TaskNotFoundError(Exception):
    pass


class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    def _row_to_task(self, row):
        return Task(
            id=row[0],
            title=row[1],
            description=row[2],
            is_completed=row[3],
            created_at=row[4]
        )

    def add_task(self, title, description=None):
        row = self.repository.create(title, description)
        return self._row_to_task(row)

    def list_tasks(self, is_completed=None):
        rows = self.repository.get_all(is_completed)
        return [self._row_to_task(row) for row in rows]

    def get_task(self, task_id):
        row = self.repository.get_by_id(task_id)

        if row is None:
            raise TaskNotFoundError

        return self._row_to_task(row)

    def update_task(self, task_id, title, description, is_completed):
        row = self.repository.update(
            task_id,
            title,
            description,
            is_completed
        )

        if row is None:
            raise TaskNotFoundError

        return self._row_to_task(row)

    def delete_task(self, task_id):
        row = self.repository.delete(task_id)

        if row is None:
            raise TaskNotFoundError

        return self._row_to_task(row)