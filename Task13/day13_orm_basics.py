from sqlalchemy import String, Integer, create_engine, select
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, Session

DATABASE_URL = "postgresql+psycopg2://postgres:sql12@localhost:5432/sqlcourse"
engine = create_engine(DATABASE_URL, echo=True)


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    country: Mapped[str | None] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"Author(id={self.id}, name={self.name!r}, country={self.country})"


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)
    author_id: Mapped[int | None] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title={self.title}, price={self.price}, author_id={self.author_id})"


# Создаём
with Session(engine) as session:
    author = Author(name="Тест Тестович", country="Тестистан")
    session.add(author)
    session.commit()
    test_id = author.id
    print(test_id)

# Читаем
with Session(engine) as session:
    author = session.get(Author, test_id)
    if author is None:
        print("Автор не найден")
    else:
        print(f"Имя автора: {author.name}\nСтрана: {author.country}")

# Обновляем
with Session(engine) as session:
    author = session.get(Author, test_id)
    assert author is not None
    author.country = "Обновлённая страна"
    session.commit()
    print(f"Имя автора: {author.name}\nСтрана: {author.country}")

# Удаляем
with Session(engine) as session:
    author = session.get(Author, test_id)
    assert author is not None
    session.delete(author)
    session.commit()

# Выводим по фильтру
with Session(engine) as session:
    stmt = select(Author).where(Author.country == "Россия")
    authors = session.execute(stmt).scalars().all()
    for a in authors:
        print(a)
