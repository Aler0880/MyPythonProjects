import sys
sys.path.append('c:\\Users\\User\\MyPythonProjects')

from Task13.day13_orm_basics import Author, Book, engine
from sqlalchemy.orm import Session
from sqlalchemy import select

with Session(engine) as session:
    author = session.get(Author, 1)
    if author is None:
        print("Автор не найден")
    else:
        print(f"Имя автора: {author.name}\nСтрана: {author.country}")

