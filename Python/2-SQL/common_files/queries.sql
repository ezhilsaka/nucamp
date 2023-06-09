--Exercise 1

CREATE TABLE cars (
	id SERIAL, 
	year INTEGER, 
	make TEXT NOT NULL, 
	Mmodel TEXT NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE drivers (
	id SERIAL, 
	car_id INT NOT NULL, 
	name TEXT NOT NULL, 
	PRIMARY KEY(id)
)

ALTER TABLE drivers ADD CONSTRAINT fk_drivers_cars FOREIGN KEY(car_id) REFERENCES cars;

--Exercise 2

CREATE TABLE events (
    id SERIAL,
    show_time TIMESTAMP,
    PRIMARY KEY (id),
	auditorium_id INT, 
	flim_id INT NOT NULL
);

CREATE TABLE auditoria (
    id SERIAL,
    capacity INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE films (
    id SERIAL,
    title TEXT NOT NULL,
    runtime INTEGER,
    PRIMARY KEY (id)
);

ALTER TABLE auditoria RENAME TO auditorium;

CREATE TABLE accounts (
   id SERIAL,
   username TEXT NOT NULL UNIQUE,
   password TEXT NOT NULL,
   PRIMARY KEY (id), 
   customer_id INT NOT NULL UNIQUE	
);

CREATE TABLE customers (
    id SERIAL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE customers_events (
    customer_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    PRIMARY KEY (customer_id, event_id)
);

ALTER TABLE events
ADD CONSTRAINT fk_events_auditoria
FOREIGN KEY (auditorium_id)
REFERENCES auditorium;

ALTER TABLE events
ADD CONSTRAINT fk_events_films
FOREIGN KEY (flim_id)
REFERENCES films;

ALTER TABLE accounts
ADD CONSTRAINT fk_accounts_customers
FOREIGN KEY (customer_id)
REFERENCES customers;

ALTER TABLE event_purchases
ADD CONSTRAINT fk_event_purchases_events
FOREIGN KEY (event_id)
REFERENCES events;

ALTER TABLE event_purchases
ADD CONSTRAINT fk_event_purchases_customers
FOREIGN KEY (customer_id)
REFERENCES customers;

-- week 2 queries --

INSERT INTO cars (year, make, model)
VALUES (2020, 'Toyoto', 'Prius'); 

DELETE FROM cars
WHERE year IS NULL; 

--insert query to insert more than one column in the same query. 
--the division is a table with id and name column
--the values for different rows should be delimited with a comma in the single query

INSERT INTO divisions (name)
VALUES ('Atlantic'),('Metropolitan'),('Pacific'),('Central');

-- CC Data Manipulation with SQL

CREATE TABLE divisions (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL UNIQUE
);

CREATE TABLE teams (
	id serial PRIMARY KEY,
	city TEXT NOT NULL,
	name TEXT NOT NULL UNIQUE,
	home_color TEXT NOT NULL,
	away_color TEXT,
	division_id INTEGER
); 

ALTER TABLE teams
ADD CONSTRAINT fk_division_id
FOREIGN KEY (division_id)
REFERENCES divisions
ON DELETE SET NULL

INSERT INTO divisions (name)
VALUES ('Atlantic'),('Metropolitan'),('Pacific'),('Central');

INSERT INTO teams (city, name, home_color, away_color, division_id)
VALUES ('New York Islanders', 'Metropolitan', 'Royal blue', 'White', 2), ('Seattle Kraken', 'Pacific', 'Deep sea Blue', 'White', 3);

UPDATE divisions SET name = 'Cosmopolitan'
WHERE name = 'Metropolitan'

DELETE FROM divisions
WHERE name = 'Cosmopolitan';

--select with alias

SELECT author as book_author, title as book_title FROM books; -- actual column names are author and title 

SELECT b.author as book_author, b.title as book_title FROM books b; 

--count with distinct

SELECT COUNT (DISTINCT genre) as genre_count FROM books; -- to count the distinct number of generes in table

--GROUP BY

SELECT genre, COUNT(*) as book_count FROM books GROUP BY genre; -- to count the number of books available for each genre

--HAVING BY

SELECT genere, COUNT(*) AS book_count -- to filter the group by result set which is having count more than 1
FROM books
GROUP BY genre
HAVING(COUNT(*)) > 1; 

--Code Challenge: Aggregate Queries

-- For each customer, list the customer_id and the order_date of their first order. Sort by customer_id.

SELECT customer_id, MIN(order_date)
FROM orders
GROUP BY customer_id
ORDER BY customer_id

-- For each customer, list customer ID and the average freight cost of their orders; sort by average freight cost.

SELECT customer_id, AVG(freight) AS avg_freight
FROM orders
GROUP BY customer_id  
ORDER BY avg_freight;


-- SET OPERATIONS

--UNION

SELECT title, president, year FROM president_books
UNION
SELECT title, author, year FROM amazon_best_sellers;

--UNION ALL 

SELECT title, president, year FROM president_books
UNION ALL
SELECT title, author, year FROM amazon_best_sellers;

--INTERSECT

SELECT title, author, year FROM amazon_best_sellers
INTERSECT
SELECT title, president AS author, year from president_books; 

--EXCEPT

SELECT title, author, year FROM amazon_best_sellers
EXCEPT
SELECT title, president AS author, year FROM president_books; 

--INNER JOIN

SELECT cc.name AS captical_city_name, c.name AS country_name
FROM captial_cities cc
INNER JOIN countries c
ON cc.country_id = c.id

-- LEFT JOIN

SELECT c.name, o.dollar_amount_spent
FROM customers c
LEFT JOIN orders o
ON o.customer_id = c.id

--RIGHT JOIN

SELECT c.name, o.dollar_amount_spent
FROM customers c
RIGHT JOIN orders o
ON o.customer_id = c.id

--FULL JOIN (same as union all)

SELECT c.name, o.dollar_amount_spent
FROM customers c
FULL JOIN orders o
ON o.customer_id = c.id

--combining set operators and joins

SELECT name FROM departments d
EXCEPT
SELECT DISTINCT name FROM departments d
INNER JOIN students s
ON s.major_department_id = d.id;

--Subqueries 

--EXISTS

SELECT a.author FROM amazon_best_sellers a
WHERE EXISTS (
    SELECT * FROM president_books b WHERE b.president = a.author
); 

--IN

SELECT a.author FROM amazon_best_sellers a
WHERE a.author IN (
    SELECT president FROM president_books 
); 

--NOT IN

SELECT a.author FROM amazon_best_sellers a
WHERE a.author NOT IN (
    SELECT president FROM president_books 
); 

--ANY

SELECT a.titile, a.year
FROM amazon_best_sellers a
WHERE a.year < ANY (
    SELECT b.year FROM president_books b
); 

--ALL

SELECT a.author FROM amazon_best_sellers a
WHERE a.author > ALL (
    SELECT b.president from president_books b
)

--WITH (To find out the duplicate last names in 2 tables and count of it)

WITH all_names AS (
	SELECT last_name FROM professors
	UNION ALL
	SELECT last_name FROM students
)
SELECT last_name, COUNT(*)
FROM all_names
GROUP BY last_name
HAVING COUNT(*) > 1; 

--WITH another example

WITH people AS (
	SELECT 'professor' AS occupation, first_name, last_name, department_id FROM professors
	UNION ALL
	SELECT 'student' AS occupation, first_name, last_name, major_department_id FROM students
)
SELECT occupation, first_name, last_name, d.code
FROM people
LEFT JOIN departments d
ON department_id = d.id; 

--INSERT QUERY with 2 Select statement subqueries

INSERT INTO employees_categories (employee_id, category_id)
SELECT e.employee_id, c.category_id
FROM employees e, categories c
WHERE e.city = 'London'
AND c.category_name = 'Dairy Products'; 

--Advanced Arithmetioc operators

WITH frames AS (
    SELECT
    CEIL(width) + 2 AS frame_width,
    CEIL(height) + 4 AS frame_height
    FROM moma_works
    WHERE classification = 'Photograph' AND width > 0 AND height > 0
)
SELECT
COUNT(*),
frame_width,
frame_height,
frame_width * frame_height AS frame_area
FROM frames
GROUP BY frame_width, frame_height, frame_area;

--JSON in postgres

SELECT jsonb_pretty(info) AS formatted_info
FROM moma_artists LIMIT 50

SELECT
info -> 'display_name' AS name,
info -> 'nationality' as nationality
FROM moma_artists
ORDER BY id
LIMIT 50;

--Different ways of inserting data in JSONB object in postgres

INSERT INTO moma_artists (info) VALUES (
    json_object('{display_name, Ablade Glover, nationality, Ghanaian}')
);

INSERT INTO moma_artists (info) VALUES (
    json_object('{{display_name, Ablade Glover}, {nationality, Ghanaian}}')
);

INSERT INTO moma_artists (info) VALUES (
    json_object('{display_name, nationality}', '{Ablade Glover, Ghanaian}')
);

--Triggers Example

CREATE FUNCTION log_new_employee() RETURNS trigger AS $$
    BEGIN
        INSERT INTO employees_log (description, employee_id) VALUES (
            'Employee created.',
            NEW.id
        );
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_new_employee AFTER INSERT ON employees
    FOR EACH ROW EXECUTE FUNCTION log_new_employee();

INSERT INTO employees (salary, name) values (55000, 'Alice');
INSERT INTO employees (salary, name) values (66000, 'Bob');

SELECT e.*, el.description, el.created_at
FROM employees_log el
JOIN employees e ON el.employee_id = e.id;

CREATE FUNCTION log_salary_update() RETURNS trigger AS $$
    BEGIN
        INSERT INTO employees_log (description, employee_id) VALUES (
            'Salary updated from '||OLD.salary||' to '||NEW.salary,
            NEW.id
        );
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_salary_update AFTER UPDATE OF salary ON employees
    FOR EACH ROW EXECUTE FUNCTION log_salary_update();

UPDATE employees SET salary = 80000 WHERE name = 'Alice';

SELECT e.*, el.description, el.created_at
FROM employees_log el
JOIN employees e ON el.employee_id = e.id;

-- Index syntax

CREATE INDEX index_name ON table_name (column_name); 

CREATE INDEX moma_works_btree_index ON moma_works(artist);

DROP INDEX moma_works_btree_index;
CREATE INDEX moma_works_hash_index ON moma_works USING HASH (artist);

--default and non default indexes

SELECT * FROM pg_indexes;

SELECT tablename, indexname, indexdef FROM pg_indexes WHERE tablename NOT LIKE 'pg_%';

-- EXPLAIN & EXPLAIN and ANALYZE

EXPLAIN SELECT date_acquired FROM moma_works 
WHERE date_acquired BETWEEN '1950-01-01' AND '1959-12-31';

EXPLAIN ANALYZE SELECT date_acquired FROM moma_works 
WHERE date_acquired BETWEEN '1950-01-01' AND '1959-12-31';

--DB Adminstration

--dump command options: docker exec pg_container pg_dump --help

--ex: docker exec pg_container pg_dump --verbose --file moma_dump.sql moma

--command to copy the dump: docker exec pg_container psql moma_copy -f moma_dump.sql





