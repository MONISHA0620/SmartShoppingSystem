DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    preferences TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL
);

-- Sample data
INSERT INTO customers (name, email, preferences)
VALUES ('John Doe', 'john@example.com', 'electronics,books');

INSERT INTO products (name, category, price) VALUES
('Wireless Mouse', 'electronics', 25.99),
('Bluetooth Headphones', 'electronics', 49.99),
('USB-C Adapter', 'electronics', 15.00),
('Python Book', 'books', 19.99),
('Notebook', 'stationery', 3.99);
