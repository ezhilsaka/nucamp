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

SELECT genere, COUNT(*) AS book_count
FROM books
GROUP BY genre
HAVING(COUNT(*)) > 1; 



