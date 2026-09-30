from fastapi import FastAPI, HTTPException
from core.tasks import TaskService, TaskNotFoundError
from schemas.task import TaskSchema, TaskCreate

app = FastAPI()

service = TaskService()
print("NEW MAIN LOADED")

@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}


@app.get("/tasks", response_model=list[TaskSchema])
def get_tasks():
    return service.list_tasks()



@app.post("/tasks", response_model=TaskSchema)
def create_task(task: TaskCreate):
    print("NEW POST VERSION")
    return service.add_task(task.title)


@app.patch("/tasks/{task_id}", response_model=TaskSchema )
def complete_task(task_id: int):
    try:
        task = service.complete_task(task_id)

        return {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }

    except TaskNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        service.delete_task(task_id)

        return {
            "message": "Task deleted"
        }

    except TaskNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )