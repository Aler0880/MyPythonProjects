import subprocess
import os
import tempfile
import random
import time
import sys

PSQL_PATH = r"C:\Program Files\PostgreSQL\18\bin\psql.exe"
DATABASE_URL = (
    "postgresql://neondb_owner:npg_T6JB4QhCdoGX@ep-small-hat-axiiwy73.c-4.us-east-2.aws.neon.tech/neondb"
    "?sslmode=require"
)

BATCH_SIZE = 100
MAX_RETRIES = 3
DELAY_BETWEEN = 0.5
RETRY_DELAY = 2

def run_sql_file(sql):
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
            env=env,
            timeout=30
        )
        if proc.returncode != 0:
            print("STDERR:", proc.stderr)
            return False
        return True
    except Exception as e:
        print("Исключение:", e)
        return False
    finally:
        if os.path.exists(fname):
            os.remove(fname)

# Создание таблицы и очистка
setup_sql = """
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INTEGER,
    pages INTEGER,
    message TEXT
);
TRUNCATE TABLE books RESTART IDENTITY;
"""
if not run_sql_file(setup_sql):
    print("❌ Ошибка при создании таблицы")
    sys.exit(1)
print("✅ Таблица создана и очищена.")

# Генерация книг
books = []
for i in range(1, 10001):
    books.append((
        f"Книга {i}",
        f"Автор {random.randint(1, 100)}",
        random.randint(1900, 2025),
        random.randint(100, 800),
        f"Описание книги {i}"
    ))
print(f"Сгенерировано {len(books)} книг.")

# Вставка
total_batches = (len(books) + BATCH_SIZE - 1) // BATCH_SIZE
print(f"Будет выполнено {total_batches} батчей по {BATCH_SIZE} книг.")
try:
    for start in range(0, len(books), BATCH_SIZE):
        batch = books[start:start+BATCH_SIZE]
        values = []
        for b in batch:
            title = b[0].replace("'", "''")
            author = b[1].replace("'", "''")
            message = b[4].replace("'", "''")
            values.append(f"('{title}', '{author}', {b[2]}, {b[3]}, '{message}')")
        sql = f"INSERT INTO books (title, author, year, pages, message) VALUES {', '.join(values)};"

        success = False
        for attempt in range(MAX_RETRIES):
            if run_sql_file(sql):
                success = True
                print(f"Вставлено {start+len(batch)} книг...")
                break
            else:
                print(f"Ошибка в батче {start//BATCH_SIZE+1}, попытка {attempt+1}. Повтор через {RETRY_DELAY} сек...")
                time.sleep(RETRY_DELAY)
        if not success:
            print(f"❌ Не удалось вставить батч {start//BATCH_SIZE+1}, прерываем.")
            break
        time.sleep(DELAY_BETWEEN)
except KeyboardInterrupt:
    print("\n⚠️  Прервано пользователем.")
    sys.exit(0)

# Дополнительные операции по отдельности
operations = [
    ("UPDATE books SET year = 2025 WHERE id = 1;", "Обновление года"),
    ("DELETE FROM books WHERE id = 2;", "Удаление книги"),
    ("SELECT '=== Итоговый список (первые 5) ===' AS info; SELECT * FROM books ORDER BY id LIMIT 5;", "Выборка первых 5"),
    ("SELECT COUNT(*) AS total FROM books;", "Подсчёт книг")
]

print("\nВыполнение дополнительных операций...")
for sql, desc in operations:
    success = False
    for attempt in range(MAX_RETRIES):
        if run_sql_file(sql):
            print(f"✅ {desc} выполнено")
            success = True
            break
        else:
            print(f"❌ Ошибка в '{desc}', попытка {attempt+1}, повтор через {RETRY_DELAY} сек...")
            time.sleep(RETRY_DELAY)
    if not success:
        print(f"❌ Не удалось выполнить '{desc}'")
        