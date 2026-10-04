from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status

from core.tasks import TaskService, TaskNotFoundError
from schemas.task import TaskCreate, TaskUpdate, TaskSchema


app = FastAPI()
service = TaskService()


@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}


@app.get("/tasks", response_model=list[TaskSchema])
def get_tasks(is_completed: Optional[bool] = None):
    return service.list_tasks(is_completed)


@app.get("/tasks/{task_id}", response_model=TaskSchema)
def get_task(task_id: int):
    try:
        return service.get_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


@app.post(
    "/tasks",
    response_model=TaskSchema,
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):
    return service.add_task(
        task.title,
        task.description
    )


@app.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task: TaskUpdate):
    try:
        return service.update_task(
            task_id,
            task.title,
            task.description,
            task.is_completed
        )
    except TaskNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(task_id: int):
    try:
        service.delete_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)