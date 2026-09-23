def add_task(tasks, title):
    tasks.append({"id": len(tasks) + 1, "title": title, "completed": False})


def list_tasks(tasks):
    for task in tasks:
        print(f"{task['id']}: {task['title']} - {task['completed']}")


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return


def delete_task(tasks, task_id):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            return
