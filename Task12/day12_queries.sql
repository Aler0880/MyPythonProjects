sqlcourse=# SELECT name, COUNT(title) AS books_count FROM authors FULL JOIN books ON authors.id = books.author_id GROUP BY name ORDER BY name
NULLS LAST;
    name     | books_count
-------------+-------------
 Гоголь      |           1
 Джойс       |           0
 Достоевский |           2
 Толстой     |           2
 Тургенев    |           1
             |           2
(6 rows)

sqlcourse=# SELECT name, ROUND(AVG(price), 2) AS avg_book_price FROM authors FULL JOIN books ON authors.id = books.author_id GROUP BY name ORD
ER BY name NULLS LAST;
    name     | avg_book_price
-------------+----------------
 Гоголь      |         800.00
 Джойс       |
 Достоевский |        1025.00
 Толстой     |        1050.00
 Тургенев    |         700.00
             |         400.00
(6 rows)

sqlcourse=# SELECT name, COUNT(title) AS books_count FROM authors FULL JOIN books ON authors.id = books.author_id GROUP BY name HAVING COUNT(t
itle) > 1 ORDER BY name NULLS LAST;
    name     | books_count
-------------+-------------
 Достоевский |           2
 Толстой     |           2
             |           2
(3 rows)
