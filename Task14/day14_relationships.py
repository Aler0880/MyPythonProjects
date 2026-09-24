import sys

sys.path.append("c:\\Users\\User\\MyPythonProjects")

from Task13.day13_orm_basics import Author, Book, engine
from sqlalchemy.orm import Session
from sqlalchemy import select

# with Session(engine) as session:
#     author = session.get(Author, 1)
#     if author is None:
#         print("Автор не найден")
#     else:
#         print(f"Имя автора: {author.name}\nСтрана: {author.country}")

# with Session(engine) as session:
#     book = session.get(Book, 7)

#     if book is None:
#         print("Книга не найдена")
#     elif book.author is None:
#         print("Автор неизвестен")
#     else:
#         print(book.author.name)

with Session(engine) as session:
    author = session.get(Author, 5)   # Джойс
    # Твоя задача: убедиться, что author.books == []
    if author is None:
        print("Автор не найден")
    else:
        print(author.books)          # Pylance доволен: здесь author точно Author
        if not author.books:
            print("У автора нет книг")
