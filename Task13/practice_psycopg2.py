import psycopg2


def connect():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="sqlcourse",
        user="postgres",
        password="sql12",
        client_encoding="UTF8",
    )


# Уязвимый вариант
def ex1a():
    conn = connect()
    cur = conn.cursor()

    def find_unsafe(name):
        sql = f"SELECT id, name, country FROM authors WHERE name = '{name}'"
        print("SQL:", sql)
        cur.execute(sql)
        return cur.fetchall()

    print("--- нормальное имя ---")
    print(find_unsafe("Толстой"))

    print("--- хакерский ввод ---")
    print(find_unsafe("' OR '1'='1"))

    cur.close()
    conn.close()


# Безопасный вариант
def ex1b():
    conn = connect()
    cur = conn.cursor()

    def find_safe(name):
        sql = "SELECT id, name, country FROM authors WHERE name = %s"
        print("SQL:", sql)
        cur.execute(sql, (name,))
        return cur.fetchall()

    print("--- нормальное имя ---")
    print(find_safe("Толстой"))

    print("--- хакерский ввод ---")
    print(find_safe("' OR '1'='1"))

    cur.close()
    conn.close()


# Точечный UPDATE
def ex2():
    conn = connect()
    cur = conn.cursor()

    # найдём id одного автора для эксперимента
    cur.execute("SELECT id FROM authors ORDER BY id LIMIT 1")
    target_id = cur.fetchone()[0]
    print("target_id =", target_id)

    # обновляем только country
    cur.execute(
        "UPDATE authors SET country = %s WHERE id = %s", ("Тест-страна", target_id)
    )
    conn.commit()

    # проверяем
    cur.execute("SELECT id, name, country FROM authors WHERE id = %s", (target_id,))
    print(cur.fetchone())

    # возвращаем как было (Россия)
    cur.execute("UPDATE authors SET country = %s WHERE id = %s", ("Россия", target_id))
    conn.commit()

    cur.close()
    conn.close()


# RETURNING
def ex3():
    conn = connect()
    cur = conn.cursor()

    print("--- вариант 1: два запроса ---")
    cur.execute(
        "INSERT INTO authors (name, country) VALUES (%s, %s)",
        ("Практик Первый", "Практика"),
    )
    conn.commit()
    cur.execute(
        "SELECT id FROM authors WHERE name = %s AND country = %s",
        ("Практик Первый", "Практика"),
    )
    id1 = cur.fetchone()[0]
    print("id1 =", id1)

    print("--- вариант 2: RETURNING ---")
    cur.execute(
        "INSERT INTO authors (name, country) VALUES (%s, %s) RETURNING id",
        ("Практик Второй", "Практика"),
    )
    id2 = cur.fetchone()[0]
    conn.commit()
    print("id2 =", id2)

    print("--- убираем за собой ---")
    cur.execute("DELETE FROM authors WHERE name LIKE %s", ("Практик%",))
    conn.commit()

    cur.close()
    conn.close()


ex1a()
