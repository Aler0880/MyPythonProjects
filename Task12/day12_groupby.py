import psycopg2

try:
    conn = psycopg2.connect(
        dbname="sqlcourse",
        user="postgres",
        password="sql12",
        host="localhost",
        port="5432",
        client_encoding="UTF8",
    )
    cur = conn.cursor()
    
    # --- ШАГ 1: Основной запрос ---
    query = """
        SELECT name, COUNT(title) AS books_count FROM authors FULL JOIN books ON authors.id = books.author_id GROUP BY name HAVING COUNT(title) > 1 ORDER BY name NULLS LAST
    """
    cur.execute(query)

    result = cur.fetchall()

    with open("C:\\Users\\User\\MyPythonProjects\\Task12\\output_day12.txt", "w", encoding="utf-8") as f:
        for name, books_count in result:
            if name == None:
                name = 'неизвестен'
            f.write(f"Автор: {name} — Книг: {books_count}\n")

    for name, books_count in result:
        if name == None:
            name = 'неизвестен'
        print(f"Автор: {name} — Книг: {books_count}\n")
    print("Готово. Результат в файле output.txt")

    cur.close()
    conn.close()

except Exception:
    import traceback

    traceback.print_exc()
