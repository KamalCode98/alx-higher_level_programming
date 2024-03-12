-- Creates a table named second_table with columns id (INT), name (VARCHAR(256)), and score (INT)
-- Inserts multiple rows into second_table
-- 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

INSERT INTO second_table(id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
