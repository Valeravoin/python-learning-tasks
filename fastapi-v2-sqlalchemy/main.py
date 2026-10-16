from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime
import json

app = FastAPI()

# --- НАСТРОЙКА БАЗЫ ДАННЫХ ---
# Это движок, который говорит: "Мы используем SQLite файл tasks.db"
# check_same_thread=False нужен только для SQLite в тестах/локально
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Фабрика сессий: создаёт "коннект" к базе, чтобы можно было делать запросы
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base — это специальный базовый класс от SQLAlchemy.
# Все твои модели (таблицы) должны наследоваться от него.
Base = declarative_base()

# ============================================================
# БЛОК 3: МОДЕЛИ. ТАБЛИЦА КАК КЛАСС PYTHON
# ============================================================

class Task(Base):
    # __tablename__ говорит SQLAlchemy, как назвать таблицу в реальной БД
    __tablename__ = "tasks"

    # Колонки описываются как атрибуты класса.
    # SQLAlchemy сам превратит их в столбцы таблицы.

    # Integer — тип данных "целое число"
    # primary_key=True — это главный ключ (уникальный ID)
    id = Column(Integer, primary_key=True, index=True)

    # String — тип данных "текст" (VARCHAR в SQL)
    title = Column(String, nullable=False)  # nullable=False значит "не может быть пустым"

    # Text — для длинных текстов (описание задачи)
    description = Column(Text, nullable=True)  # nullable=True значит "может быть пустым"

    # Boolean — тип "да/нет" (True/False)
    is_done = Column(Boolean, default=False)

    # DateTime — тип "дата и время"
    created_at = Column(DateTime, default=datetime.utcnow)

    # Priority — число от 1 до 5
    priority = Column(Integer, default=1)

    # Tags — храним как JSON-строку (для простоты в SQLite без расширений)
    tags = Column(Text, nullable=True)

# Создаём все таблицы, описанные в моделях (в данном случае — таблицу tasks)
Base.metadata.create_all(bind=engine)

# ============================================================
# PYDANTIC МОДЕЛИ (ДЛЯ API)
# ============================================================

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3)
    tags: list[str] = []
    priority: int = Field(default=1, ge=1, le=5)
    description: str | None = None
    is_done: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str
    tags: list[str]
    priority: int
    description: str | None
    is_done: bool
    created_at: datetime

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # Превращаем список тегов в JSON-строку для хранения в колонке Text
    tags_json = json.dumps(task.tags)

    # Создаём объект Python (экземпляр класса Task)
    # Это и есть "база данных как объект"
    db_task = Task(
        title=task.title,
        tags=tags_json,
        priority=task.priority,
        description=task.description,
        is_done=task.is_done
        # created_at заполнится автоматически благодаря default=datetime.utcnow
    )

    # Добавляем объект в сессию (пока только в память Python)
    db.add(db_task)
    
    # Сохраняем в реальную базу данных (делаем COMMIT)
    db.commit()
    
    # Обновляем объект данными из БД (там появится реальный ID)
    db.refresh(db_task)

    return TaskResponse(
        id=db_task.id,
        title=db_task.title,
        tags=json.loads(db_task.tags) if db_task.tags else [],
        priority=db_task.priority,
        description=db_task.description,
        is_done=db_task.is_done,
        created_at=db_task.created_at
    )

@app.get("/")
def root():
    return {"message": "Блок 3: SQLAlchemy ORM работает!"}
