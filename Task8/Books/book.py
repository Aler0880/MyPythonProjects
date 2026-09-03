class Book:
    def __init__(self, title, author, year, pages, message=""):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.message = message

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @property
    def message(self):
        return self._message

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Название не может быть пустым")
        self._title = value

    @author.setter
    def author(self, value):
        if not value.strip():
            raise ValueError("Название не может быть пустым")
        self._author = value

    @year.setter
    def year(self, value):
        if not 0 < value <= 2026:
            raise ValueError("Год должен быть в диапазоне от 0 до 2026")
        self._year = value

    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = value

    @message.setter
    def message(self, value):
        self._message = value

    def info(self):
        return (
            f"\n\nНазвание: {self.title}\nАвтор: {self.author}\n"
            f"Год издания: {self.year}\nКол-во страниц: {self.pages}\nОсновной посыл: {self.message}"
        )

    def is_long(self):
        return self.pages > 300

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "pages": self.pages,
            "message": self.message,
        }

    def __repr__(self):
        return (
            f'Book(Название: "{self.title}", Автор: {self.author}, Год издания: {self.year}, Кол-во страниц: {self.pages}, '
            f"Посыл: {self.message}"
        )