# Импортируем всё, что нужно для SQLAlchemy 2.0
from sqlalchemy import create_engine, select, func, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


# Базовый класс для всех наших моделей
class Base(DeclarativeBase):
    pass


# Модель User — описывает таблицу user в базе данных
class User(Base):
    __tablename__ = "user"

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age})"

    # Колонка id: целое число, первичный ключ
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Колонка name: строка
    name: Mapped[str] = mapped_column(String)

    # Колонка age: целое число
    age: Mapped[int] = mapped_column(Integer)


# Создаём движок SQLite в памяти.
# echo=True будет печатать SQL-запросы в консоль — удобно для обучения.
engine = create_engine("sqlite:///:memory:", echo=True)

# Создаём все таблицы, которые описаны в моделях
Base.metadata.create_all(engine)


# Открываем сессию — посредника между кодом и базой
with Session(engine) as session:
    # Добавляем двух пользователей
    session.add_all([
        User(name="Аня", age=25),
        User(name="Борис", age=30),
    ])

    # Фиксируем изменения в базе
    session.commit()

    # ============================================================
    # ПРИМЕР 1. Чтение всех объектов User через execute -> scalars -> all
    # ============================================================

    # select(User) — описываем запрос: выбрать все объекты User.
    # session.execute(...) — выполняем запрос, получаем объект Result.
    # .scalars() — из каждой строки достаём один главный объект (User).
    # .all() — собираем все объекты в список.
    users = session.execute(select(User)).scalars().all()

    print("Пример 1. Все пользователи:")
    print(users)
    # Вывод: [User(id=1, name='Аня', age=25), User(id=2, name='Борис', age=30)]

    # Можно перебрать список и обратиться к полям объектов
    for user in users:
        print(f"  {user.id}: {user.name}, возраст {user.age}")

    # ============================================================
    # ПРИМЕР 2. То же самое, но короче через session.scalars
    # ============================================================

    # session.scalars(select(User)) — это сокращение для execute + scalars.
    # Затем .all() собирает результат в список.
    users_short = session.scalars(select(User)).all()

    print("\nПример 2. То же самое, но короче:")
    print(users_short)

    # ============================================================
    # ПРИМЕР 3. Что будет, если НЕ использовать scalars
    # ============================================================

    # Здесь мы не вызываем scalars, поэтому получаем список объектов Row.
    # Row — это обёртка вокруг одной строки результата.
    rows = session.execute(select(User)).all()

    print("\nПример 3. Без scalars — получаем Row:")
    print(rows)
    # Вывод: [(User(id=1, name='Аня', age=25),), (User(id=2, name='Борис', age=30),)]

    # В каждой строке лежит один объект User, но он упакован в Row.
    # Чтобы достать User, нужно обратиться по индексу 0.
    for row in rows:
        user = row[0]          # достаём User из обёртки Row
        print(f"  {user.name}, возраст {user.age}")

    # ============================================================
    # ПРИМЕР 4. Чтение одной колонки — только имена
    # ============================================================

    # select(User.name) — выбираем только колонку name.
    # В каждой строке будет одно значение — имя.
    # scalars() достаёт это одно значение из каждой строки.
    names = session.execute(select(User.name)).scalars().all()

    print("\nПример 4. Только имена:")
    print(names)
    # Вывод: ['Аня', 'Борис']

    # ============================================================
    # ПРИМЕР 5. Чтение нескольких колонок — имя и возраст
    # ============================================================

    # Здесь scalars() НЕ подходит, потому что в каждой строке два значения.
    # Если вызвать scalars(), то останется только первое значение — имя.
    # Поэтому используем просто execute и all.
    rows = session.execute(select(User.name, User.age)).all()

    print("\nПример 5. Несколько колонок:")
    for name, age in rows:
        print(f"  {name}, {age}")

    # ============================================================
    # ПРИМЕР 6. Несколько колонок в виде словарей через mappings
    # ============================================================

    # .mappings() превращает каждую строку в словарь.
    # Ключи — имена колонок.
    dict_rows = session.execute(select(User.name, User.age)).mappings().all()

    print("\nПример 6. Несколько колонок как словари:")
    for row in dict_rows:
        print(f"  {row['name']}, {row['age']}")

    # ============================================================
    # ПРИМЕР 7. Получить первого пользователя или None
    # ============================================================

    # .first() возвращает первый объект или None, если ничего нет.
    first_user = session.execute(select(User)).scalars().first()

    print("\nПример 7. Первый пользователь:")
    print(first_user)
    # Вывод: User(id=1, name='Аня', age=25)

    # ============================================================
    # ПРИМЕР 8. Получить одно значение — количество пользователей
    # ============================================================

    # select(func.count()).select_from(User) — запрос на количество строк.
    # .scalar_one() возвращает ровно одно значение.
    # Если строк окажется не одна, будет ошибка.
    count = session.execute(
        select(func.count()).select_from(User)
    ).scalar_one()

    print("\nПример 8. Количество пользователей:")
    print(count)
    # Вывод: 2

    # ============================================================
    # ПРИМЕР 9. Итерация без all — экономим память
    # ============================================================

    # Можно не вызывать all(), а сразу перебирать результат в цикле.
    # Это удобно, если записей очень много.
    print("\nПример 9. Перебор без all:")
    for user in session.execute(select(User)).scalars():
        print(f"  {user.name}")