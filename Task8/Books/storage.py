import json
from books.book import Book


def save_books(books, filename):
    data = []
    for book in books:
        data.append(
            {
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "pages": book.pages,
                "message": book.message,
            }
        )
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_books(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    books = []
    for item in data:
        book = Book(
            title=item["title"],
            author=item["author"],
            year=item["year"],
            pages=item["pages"],
            message=item["message"],
        )
        books.append(book)
    return books
