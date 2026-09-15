import psycopg

try:
    conn = psycopg.connect(
        dbname="sqlcourse",
        user="postgres",
        password="sql12",
        host="localhost",
        port="5432",
        client_encoding="UTF8",
    )
    cur = conn.cursor()

    # --- ШАГ 1: Очистить таблицы ---
    cur.execute("DELETE FROM books")
    cur.execute("DELETE FROM authors")
    cur.execute("ALTER SEQUENCE authors_id_seq RESTART WITH 1")
    cur.execute("ALTER SEQUENCE books_id_seq RESTART WITH 1")

    # --- ШАГ 2: Вставить авторов ---
    authors_data = [
        ("Толстой", "Россия"),
        ("Тургенев", "Россия"),
        ("Достоевский", "Россия"),
        ("Гоголь", "Россия"),
        ("Джойс", "Ирландия"),
    ]
    for name, country in authors_data:
        cur.execute(
            "INSERT INTO authors (name, country) VALUES (%s, %s)", (name, country)
        )

    # --- ШАГ 3: Вставить книги ---
    books_data = [
        ("Война и мир", 1200.00, 1869, 1),
        ("Анна Каренина", 900.00, 1877, 1),
        ("Отцы и дети", 700.00, 1862, 2),
        ("Преступление и наказание", 1100.00, 1866, 3),
        ("Идиот", 950.00, 1869, 3),
        ("Мёртвые души", 800.00, 1842, 4),
        ("Анонимная рукопись", 500.00, 1900, None),
        ("Загадочный фолиант", 300.00, None, None),
    ]
    for title, price, year, author_id in books_data:
        cur.execute(
            "INSERT INTO books (title, price, year, author_id) VALUES (%s, %s, %s, %s)",
            (title, price, year, author_id),
        )

    conn.commit()

    # --- ШАГ 4: Проверка ---
    cur.execute("SELECT name FROM authors WHERE id = 1")
    print("Проверка:", cur.fetchone())

    # --- ШАГ 5: Основной запрос ---
    query = """
        SELECT a.name,
               (SELECT COUNT(*) FROM books b WHERE b.author_id = a.id) AS book_count
        FROM authors a
    """
    cur.execute(query)

    with open("output.txt", "w", encoding="utf-8") as f:
        for name, count in cur.fetchall():
            f.write(f"Автор: {name} — Книг: {count}\n")

    cur.close()
    conn.close()
    print("Готово. Результат в файле output.txt")

except Exception:
    import traceback

    traceback.print_exc()
