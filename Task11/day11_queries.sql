-- День 11. Подзапросы

-- 1. IN: авторы с книгами
SELECT name FROM authors WHERE id IN (SELECT author_id FROM books);

-- 2. NOT IN: авторы без книг (вернёт 0 из-за NULL)
SELECT name FROM authors WHERE id NOT IN (SELECT author_id FROM books);

-- 3. EXISTS: авторы с книгами
SELECT a.name FROM authors a
WHERE EXISTS (SELECT 1 FROM books b WHERE b.author_id = a.id);

-- 4. NOT EXISTS: авторы без книг
SELECT a.name FROM authors a
WHERE NOT EXISTS (SELECT 1 FROM books b WHERE b.author_id = a.id);

-- 5. Скалярный: книги дороже средней цены
SELECT title, price FROM books
WHERE price > (SELECT AVG(price) FROM books);

-- 6. Подзапрос в SELECT: имя автора + количество книг
SELECT a.name,
       (SELECT COUNT(*) FROM books b WHERE b.author_id = a.id) AS book_count
FROM authors a;

-- 7. JOIN-эквивалент п.1
SELECT DISTINCT a.name FROM authors a
JOIN books b ON a.id = b.author_id;

EXPLAIN ANALYZE
SELECT name FROM authors
WHERE id IN (SELECT author_id FROM books);

EXPLAIN ANALYZE
SELECT a.name FROM authors a
WHERE EXISTS (SELECT 1 FROM books b WHERE b.author_id = a.id);

-- Альтернатива NOT IN, устойчивая к NULL:
SELECT a.name
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
WHERE b.author_id IS NULL;

Запрос №5 (скалярный) можно усилить. Сейчас он возвращает книги дороже средней. Добавь проверку на NULL в price, если такие данные возможны:

SELECT title, price
FROM books
WHERE price > (SELECT AVG(price) FROM books)
  AND price IS NOT NULL;