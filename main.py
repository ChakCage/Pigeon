from core.tasks import add_task, complete_task, delete_task, list_tasks


def main():
    tasks = []

    add_task(tasks, "Learn Python")
    add_task(tasks, "Build Todo List")
    add_task(tasks, "Practice Git")
    assert tasks == [
        {"id": 1, "title": "Learn Python", "completed": False},
        {"id": 2, "title": "Build Todo List", "completed": False},
        {"id": 3, "title": "Practice Git", "completed": False},
    ]
    print("All tasks:")
    list_tasks(tasks)

    complete_task(tasks, 2)
    assert tasks[1]["completed"] is True
    print("\nAfter completing task 2:")
    list_tasks(tasks)

    delete_task(tasks, 1)
    assert [task["id"] for task in tasks] == [2, 3]
    print("\nAfter deleting task 1:")
    list_tasks(tasks)

    complete_task(tasks, 999)
    delete_task(tasks, 999)
    assert tasks == [
        {"id": 2, "title": "Build Todo List", "completed": True},
        {"id": 3, "title": "Practice Git", "completed": False},
    ]
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
