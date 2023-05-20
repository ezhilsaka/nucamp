-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS week1_workshop;
CREATE DATABASE week1_workshop;
-- connect via psql
\c week1_workshop

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
---

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY (id)
);


CREATE TABLE categories (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);

-- TODO create more tables here...

CREATE TABLE suppliers (
    id SERIAL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE customers (
    id SERIAL,
    company_name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE employees (
    id SERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE orders (
    id SERIAL,
    date_value DATE,
    customer_id INTEGER NOT NULL,
    employee_id INTEGER,
    PRIMARY KEY (id)
);

CREATE TABLE orders_products (
    product_id INTEGER,
    order_id INTEGER,
    quantity INTEGER NOT NULL,
    discount NUMERIC NOT NULL,
    PRIMARY KEY (product_id, order_id)
);

CREATE TABLE territories (
    id SERIAL,
    territory_description TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE employees_territories (
    employee_id INTEGER NOT NULL,
    territory_id INTEGER NOT NULL,
    PRIMARY KEY (employee_id, territory_id)
);

CREATE TABLE offices (
    id SERIAL,
    address_line TEXT NOT NULL,
    territory_id INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE us_states (
    id SERIAL,
    name TEXT NOT NULL,
    abbreviation CHARACTER(2) NOT NULL,
    PRIMARY KEY (id)
);

---
--- Add foreign key constraints
---

-- PRODUCTS

ALTER TABLE products
ADD CONSTRAINT fk_products_categories 
FOREIGN KEY (category_id) 
REFERENCES categories (id);

-- TODO create more constraints here...

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customers 
FOREIGN KEY (customer_id) 
REFERENCES customers;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_employees 
FOREIGN KEY (employee_id) 
REFERENCES employees;

ALTER TABLE products
ADD CONSTRAINT fk_products_suppliers 
FOREIGN KEY (supplier_id) 
REFERENCES suppliers;

ALTER TABLE orders_products
ADD CONSTRAINT fk_orders_products_orders 
FOREIGN KEY (order_id) 
REFERENCES orders;

ALTER TABLE orders_products
ADD CONSTRAINT fk_orders_products_products 
FOREIGN KEY (product_id) 
REFERENCES products;

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_employees 
FOREIGN KEY (employee_id) 
REFERENCES employees;

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_territories 
FOREIGN KEY (territory_id) 
REFERENCES territories;

ALTER TABLE offices
ADD CONSTRAINT fk_offices_territories 
FOREIGN KEY (territory_id) 
REFERENCES territories;

--Bonus Task

ALTER TABLE employees
ADD COLUMN reports_to INTEGER;

ALTER TABLE employees
ADD CONSTRAINT fk_employees_report_to
FOREIGN KEY (reports_to)
REFERENCES employees; 