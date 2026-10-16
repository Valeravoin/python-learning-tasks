# test_crud.py — скрипт для тренировки CRUD без сервера

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from models import Task, Base  # импортируем нашу модель и Base

# --- 1. ПОДКЛЮЧЕНИЕ К БАЗЕ ---
# sqlite:///tasks.db — база создастся в той папке, где запущен этот скрипт
SQLALCHEMY_DATABASE_URL = "sqlite:///tasks.db"

# create_engine — это «дверь» в базу данных
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # обязательно для SQLite + многопоточности
)

# SessionLocal — фабрика, которая делает сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print("✅ Подключились к базе данных.")


# --- 2. СОЗДАНИЕ ТАБЛИЦ (create_all) ---
# Если таблицы ещё нет — она создастся. Если есть — ничего страшного, просто пропустит.
Base.metadata.create_all(bind=engine)
print("✅ Таблицы проверены/созданы.")


# --- 3. ДОБАВЛЕНИЕ 3 ЗАДАЧ (CREATE) ---
with SessionLocal() as session:
    # Задача 1
    task1 = Task(
        title="Изучить SQLAlchemy",
        tags="orm,learning",
        priority=5,
        is_done=False
    )
    session.add(task1)

    # Задача 2
    task2 = Task(
        title="Сделать мини-проект для портфолио",
        tags="portfolio,freelance",
        priority=4,
        is_done=False
    )
    session.add(task2)

    # Задача 3
    task3 = Task(
        title="Разобрать CRUD операции",
        tags="crud,practice",
        priority=3,
        is_done=True
    )
    session.add(task3)

    # commit — фиксируем все три задачи в базе
    session.commit()
    
    # refresh — просим базу дать реальные ID, которые она присвоила
    session.refresh(task1)
    session.refresh(task2)
    session.refresh(task3)

    print(f"✅ Созданы задачи: {task1.id}, {task2.id}, {task3.id}")


# --- 4. SELECT: ВЫВЕСТИ ВСЕ ЗАДАЧИ (READ) ---
with SessionLocal() as session:
    all_tasks = session.query(Task).all()  # .all() = «дай мне всё»
    
    print("\n📋 Все задачи в базе:")
    for t in all_tasks:
        status = "✅ Готово" if t.is_done else "⏳ В работе"
        print(f"ID: {t.id} | {t.title} | Приоритет: {t.priority} | Теги: {t.tags} | Статус: {status}")


# --- 5. ПОИСК ПО ТЕГУ (FILTER) ---
search_tag = "freelance"
print(f"\n🔍 Ищем задачи с тегом '{search_tag}':")

with SessionLocal() as session:
    # Простой поиск по подстроке в поле tags
    # like('%freelance%') означает «содержит freelance где-то внутри»
    found_tasks = session.query(Task).filter(Task.tags.like(f"%{search_tag}%")).all()

    if found_tasks:
        for t in found_tasks:
            print(f"→ Найдена: {t.title} (ID: {t.id})")
    else:
        print("→ Ничего не найдено.")
