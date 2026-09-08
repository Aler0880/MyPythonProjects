import subprocess
import os
import tempfile

PSQL_PATH = r"C:\Program Files\PostgreSQL\18\bin\psql.exe"
DATABASE_URL = (
    "postgresql://neondb_owner:npg_T6JB4QhCdoGX@ep-small-hat-axiiwy73.c-4.us-east-2.aws.neon.tech/neondb"
    "?sslmode=require"
)

# Список SQL-команд (каждая — отдельная строка, как в исходнике)
commands = [
    "CREATE TABLE IF NOT EXISTS books ("
    "id SERIAL PRIMARY KEY,"
    "title VARCHAR(255) NOT NULL,"
    "author VARCHAR(255) NOT NULL,"
    "year INTEGER,"
    "pages INTEGER,"
    "message TEXT"
    ");",

    "TRUNCATE TABLE books RESTART IDENTITY;",

    "INSERT INTO books (title, author, year, pages, message) VALUES "
    "('Название книги 1', 'Автор 1', 2020, 350, 'Краткое описание'), "
    "('Название книги 2', 'Автор 2', 2018, 420, 'Другое описание'), "
    "('Название книги 3', 'Автор 3', 2021, 280, 'Ещё одно описание');",

    "INSERT INTO books (title, author, year, pages, message) VALUES "
    "('1984', 'George Orwell', 1949, 328, 'Роман-антиутопия');",

    "SELECT '=== Список всех книг (после добавления) ===' AS info;"
    " SELECT * FROM books ORDER BY id;",

    "UPDATE books SET year = 2025 WHERE id = 1;"
    " SELECT '=== Год книги с id=1 обновлён на 2025 ===' AS info;",

    "DELETE FROM books WHERE id = 2;"
    " SELECT '=== Книга с id=2 удалена ===' AS info;",

    "SELECT '=== Итоговый список книг (после обновления и удаления) ===' AS info;"
    " SELECT * FROM books ORDER BY id;",
]

# Функция для выполнения одной команды через временный файл
def run_sql(sql):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.sql', delete=False, encoding='utf-8') as f:
        f.write(sql)
        fname = f.name

    env = os.environ.copy()
    env["PGCLIENTENCODING"] = "UTF8"
    env["LC_MESSAGES"] = "C"

    try:
        proc = subprocess.run(
            [PSQL_PATH, "-d", DATABASE_URL, "-f", fname, "--no-psqlrc", "-q"],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            env=env
        )
        if proc.stdout:
            print(proc.stdout)
        if proc.returncode != 0:
            print(f"Ошибка в команде:\n{sql}\n{proc.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Исключение: {e}")
        return False
    finally:
        if os.path.exists(fname):
            os.remove(fname)

# Основная часть
print("Выполнение команд...\n")
for i, cmd in enumerate(commands, 1):
    print(f"--- Команда {i} ---")
    if not run_sql(cmd):
        print("Прерывание из-за ошибки.")
        break
else:
    print("\n✅ Все команды выполнены успешно!")
    