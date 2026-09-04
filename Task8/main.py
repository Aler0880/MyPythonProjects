# Task8/main.py

from books.book import Book
from books.storage import save_books, load_books
from vectors.vector import Vector2D

# --- Работа с книгами ---
print("=== Книги ===")

book1 = Book(
    "Война и мир",
    "Лев Толстой",
    1869,
    1225,
    "Истинная жизнь — в простых человеческих чувствах и семейных ценностях, а не в историческом величии.",
)
book2 = Book(
    "Преступление и наказание",
    "Фёдор Достоевский",
    1866,
    671,
    "Освобождение от зла приходит только через искреннее раскаяние и принятие страдания.",
)
book3 = Book(
    "Тихий Дон",
    "Михаил Шолохов",
    1940,
    1360,
    "Человек оказывается бессильной жертвой истории, и спасение возможно лишь в возвращении к родной земле и дому.",
)

books = [book1, book2, book3]

save_books(books, "books.json")
print("Книги сохранены в books.json", end="\n\n")

loaded = load_books("books.json")
print("Загруженные книги:", end="\n\n")
for b in loaded:
    print(b, "\n\n")

# --- Работа с векторами ---
print("\n=== Векторы ===", end="\n\n")

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

v3 = v1 + v2
print(f"{v1} + {v2} = {v3}", end="\n\n")

v4 = v1 - v2
v5 = v1 * 2
print(f"{v1} - {v2} = {v4}", end="\n\n")
print(f"{v1} * 2 = {v5}", end="\n\n")
