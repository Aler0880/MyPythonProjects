import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="books_db",
        user="postgres",
        password="sql12",
        port=5432,
    )
    return conn


if __name__ == "__main__":
    conn = get_connection()  # вызываем нашу функцию
    cursor = conn.cursor()  # создаём курсор

request = "WHERE year > 1950"
print(request)
print("Книги, изданные после этого года:")

cursor.execute(f"SELECT * FROM books {request};")  # твой SQL-запрос

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
    print("")

    header = " | ".join(
        col_name.ljust(col_widths[i]) for i, col_name in enumerate(column_names)
    )
    print(header)
    print("-" * len(header))  # разделитель той же длины

    # Вывод строк
    for row in str_rows:
        row_str = " | ".join(value.ljust(col_widths[i]) for i, value in enumerate(row))
        print(row_str)
else:
    print("Нет данных")

print("\n", "*" * 50, "\n")

##################################################################

request = "WHERE pages > 500"
print(request)
print('Книги больше стольки страниц:')

cursor.execute(f"SELECT * FROM books {request};")  # твой SQL-запрос

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
    print("")

    header = " | ".join(
        col_name.ljust(col_widths[i]) for i, col_name in enumerate(column_names)
    )
    print(header)
    print("-" * len(header))  # разделитель той же длины

    # Вывод строк
    for row in str_rows:
        row_str = " | ".join(value.ljust(col_widths[i]) for i, value in enumerate(row))
        print(row_str)
else:
    print("Нет данных")

print("\n", "*" * 50, "\n")

##################################################################

request = "ORDER BY year ASC"
print(request)
print("Сортировка по году издания (ACS - возрастание, DECS - убывание):")

cursor.execute(f"SELECT * FROM books {request};")  # твой SQL-запрос

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
    print("")

    header = " | ".join(
        col_name.ljust(col_widths[i]) for i, col_name in enumerate(column_names)
    )
    print(header)
    print("-" * len(header))  # разделитель той же длины

    # Вывод строк
    for row in str_rows:
        row_str = " | ".join(value.ljust(col_widths[i]) for i, value in enumerate(row))
        print(row_str)
else:
    print("Нет данных")

print("\n", "*" * 50, "\n")

##################################################################

request = "ORDER BY pages DESC LIMIT 3"
print(request)
print("Самых толстых (DECS) или тонких (ACS) N книг:")

cursor.execute(f"SELECT * FROM books {request};")  # твой SQL-запрос

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
    print("")

    header = " | ".join(
        col_name.ljust(col_widths[i]) for i, col_name in enumerate(column_names)
    )
    print(header)
    print("-" * len(header))  # разделитель той же длины

    # Вывод строк
    for row in str_rows:
        row_str = " | ".join(value.ljust(col_widths[i]) for i, value in enumerate(row))
        print(row_str)
else:
    print("Нет данных")

print("\n", "*" * 50, "\n")

##################################################################

request = "SELECT COUNT(*) FROM books;"
print(request, "\n")

cursor.execute(f"{request};")  # твой SQL-запрос

print("Всего книг: ", cursor.fetchall()[0][0])

print("\n", "*" * 50, "\n")


##################################################################

request = "SELECT AVG(pages) FROM books;"
print(request, "\n")

cursor.execute(f"{request};")  # твой SQL-запрос

print(f"Cреднее количество страниц по всем книгам: {cursor.fetchall()[0][0]:.2f}")

print("\n", "*" * 50, "\n")


cursor.close()
conn.close()
