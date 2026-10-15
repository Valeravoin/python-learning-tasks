from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    tags: List[str]
    priority: int = 1
    description: Optional[str] = None
    is_done: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str
    tags: List[str]
    priority: int
    description: Optional[str]
    is_done: bool    

@app.get("/")
def read_root():
    return {"message": "Я победил ошибку с reload, УРААА!"}

@app.get("/tasks")
def list_tasks(tag: str | None = None, min_length: int | None = None, status: str | None = None):
    fake_tasks = [
        {"id": 1, "title": "Изучить основы Git", "tag": "git", "status": "tobo"},
        {"id": 2, "title": "Написать бота на aiogram", "tag": "telegram", "status": "in_progress"},
        {"id": 3, "title": "Сделать CRUD на FastAPI", "tag": "fastapi", "status": "done"}
    ]

    if tag:
        fake_tasks = [t for t in fake_tasks if t["tag"] == tag]

    if status:
        fake_tasks = [t for t in fake_tasks if t["status"] == status]

    if min_length is not None:
        fake_tasks = [t for t in fake_tasks if len(t["title"]) >= min_length]

    return {
        "filter": {
            "tag": tag,
            "status": status
        },
        "results": fake_tasks
    }

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    return {
        "id": task_id,
        "message": f"Ты запросил задачу с ID {task_id}",
        "example_data": {
            "title": "Пример задачи",
            "tag": "learning"
        }
    }

@app.post("/tasks", response_model=TaskResponse)
def create_new_task(task: TaskCreate) -> TaskResponse:
    new_id = 999
    return TaskResponse(
        id=new_id,
        title=task.title,
        tags=task.tags,
        priority=task.priority,
        description=task.description,
        is_done=task.is_done
    )

@app.post("/tasks/with-filter")
def create_task_with_filter(
    task: TaskCreate,
    force_tag: str | None = None
):
    # Исправлено: обращаемся к task.tags (список), а не task.tag
    result = {
        "message": "Задача создана с фильтром",
        "received_from_body": {
            "title": task.title,
            "tags": task.tags
        },
        "received_from_url": {
            "force_tag": force_tag
        }
    }

    if force_tag is not None:
        result["final_tag"] = force_tag
    else:
        # Безопасно берём первый тег из списка
        result["final_tag"] = task.tags[0] if task.tags else None

    return result
