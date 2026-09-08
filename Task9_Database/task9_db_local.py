import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="localhost", database="books_db", user="postgres", password="sql12"
    )
    return conn


if __name__ == "__main__":
    conn = get_connection()  # вызываем нашу функцию
    cursor = conn.cursor()  # создаём курсор

    books_data = [
        ("Название книги 1", "Автор 1", 2020, 350, "Краткое описание"),
        ("Название книги 2", "Автор 2", 2018, 420, "Другое описание"),
        ("Название книги 3", "Автор 3", 2021, 280, "Ещё одно описание"),
    ]

    cursor.execute("TRUNCATE TABLE books RESTART IDENTITY;")  # очистить таблицу и сбросить id

    for book in books_data:
        cursor.execute(
            """
            INSERT INTO books (title, author, year, pages, message)
            VALUES (%s, %s, %s, %s, %s)
        """,
            book,
        )

    conn.commit()

    cursor.execute("SELECT * FROM books;")

    # ... после cursor.execute и fetchall

    if cursor.description is not None:
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        # Преобразуем все значения в строки
        str_rows = [[str(item) for item in row] for row in rows]

        # Вычисляем ширину столбцов
        col_widths = []
        for i in range(len(column_names)):
            max_len = len(column_names[i])
            for row in str_rows:
                if len(row[i]) > max_len:
                    max_len = len(row[i])
            col_widths.append(max_len)

        # Вывод заголовка
        header = " | ".join(
            col_name.ljust(col_widths[i]) for i, col_name in enumerate(column_names)
        )
        print(header)
        print("-" * len(header))  # разделитель той же длины

        # Вывод строк
        for row in str_rows:
            row_str = " | ".join(
                value.ljust(col_widths[i]) for i, value in enumerate(row)
            )
            print(row_str)
    else:
        print("Нет данных")

    cursor.close()
    conn.close()