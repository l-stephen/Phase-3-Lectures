-- use .read filename to run this file!

-- sqlite3 <databasename>.db to create a database
-- Drop tables if they exist
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;

-- Create tables
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    total_price REAL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert sample data
INSERT INTO customers(name, email)
VALUES ('John Doe', 'john@example.com'),
       ('Jane Smith', 'jane@example.com'),
       ('Michael Johnson', 'michael@example.com');

INSERT INTO products(name, price)
VALUES ('Smartwatch', 199.99),
       ('Wireless Earbuds', 79.99),
       ('Digital Camera', 299.99),
       ('Fitness Tracker', 129.99),
       ('Bluetooth Speaker', 149.99);

INSERT INTO orders(customer_id, product_id, quantity, total_price, order_date)
VALUES (1, 1, 1, 199.99, '2024-02-07'),
       (2, 2, 2, 159.98, '2024-02-07'),
       (3, 3, 1, 199.99, '2024-02-07'),
       (1, 4, 1, 129.99, '2024-02-07'),
       (2, 5, 2, 299.98, '2024-02-07');
