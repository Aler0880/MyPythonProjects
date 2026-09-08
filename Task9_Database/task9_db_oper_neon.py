import subprocess
import os
import tempfile
import time
import sys

PSQL_PATH = r"C:\Program Files\PostgreSQL\18\bin\psql.exe"
DATABASE_URL = (
    "postgresql://neondb_owner:npg_T6JB4QhCdoGX@ep-small-hat-axiiwy73.c-4.us-east-2.aws.neon.tech/neondb"
    "?sslmode=require"
)

MAX_RETRIES = 3
RETRY_DELAY = 2

def run_sql_file(sql):
    """Выполняет SQL-команду через временный файл."""
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
        print(proc.stdout)   # выводим результат SELECT'ов
        return True
    except Exception as e:
        print("Исключение:", e)
        return False
    finally:
        if os.path.exists(fname):
            os.remove(fname)

# Список операций (SQL и описание)
operations = [
    ("UPDATE books SET year = 2025 WHERE id = 1;", "Обновление года у книги с id=1"),
    ("DELETE FROM books WHERE id = 2;", "Удаление книги с id=2"),
    ("SELECT '=== Первые 5 книг ===' AS info; SELECT * FROM books ORDER BY id LIMIT 5;", "Выборка первых 5 книг"),
    ("SELECT COUNT(*) AS total FROM books;", "Подсчёт общего количества книг")
]

print("Выполнение операций с базой данных...\n")

for sql, desc in operations:
    success = False
    for attempt in range(MAX_RETRIES):
        print(f"▶ {desc} (попытка {attempt+1})...")
        if run_sql_file(sql):
            print(f"✅ {desc} выполнено успешно.\n")
            success = True
            break
        else:
            print(f"❌ Ошибка, повтор через {RETRY_DELAY} сек...\n")
            time.sleep(RETRY_DELAY)
    if not success:
        print(f"❌ Не удалось выполнить: {desc}\n")

print("Готово.")
