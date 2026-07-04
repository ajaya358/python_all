# SQL Basics - Core queries every developer must know

print("=== CREATE TABLE ===")
create = """
CREATE TABLE users (
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(100) NOT NULL,
    email    VARCHAR(150) UNIQUE NOT NULL,
    age      INTEGER,
    created  TIMESTAMP DEFAULT NOW()
);

CREATE TABLE orders (
    id         SERIAL PRIMARY KEY,
    user_id    INTEGER REFERENCES users(id),
    product    VARCHAR(100),
    amount     DECIMAL(10,2),
    created    TIMESTAMP DEFAULT NOW()
);
"""
print(create)

print("=== INSERT ===")
insert = """
INSERT INTO users (name, email, age) VALUES ('Ajay', 'ajay@email.com', 25);
INSERT INTO users (name, email, age) VALUES ('Ravi', 'ravi@email.com', 30);
INSERT INTO users (name, email, age) VALUES ('Priya', 'priya@email.com', 22);
"""
print(insert)

print("=== SELECT ===")
select = """
SELECT * FROM users;                          -- all rows, all columns
SELECT name, email FROM users;                -- specific columns
SELECT * FROM users WHERE age > 24;           -- filter
SELECT * FROM users WHERE name LIKE 'A%';     -- pattern match
SELECT * FROM users ORDER BY age DESC;        -- sort
SELECT * FROM users LIMIT 10 OFFSET 0;        -- pagination
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
"""
print(select)

print("=== UPDATE ===")
update = """
UPDATE users SET age = 26 WHERE id = 1;
UPDATE users SET name = 'Ajay Kumar', age = 27 WHERE email = 'ajay@email.com';
"""
print(update)

print("=== DELETE ===")
delete = """
DELETE FROM users WHERE id = 3;
DELETE FROM users WHERE age < 18;
"""
print(delete)

print("=== AGGREGATE FUNCTIONS ===")
aggregate = """
SELECT COUNT(*) FROM users;                   -- total rows
SELECT AVG(age) FROM users;                   -- average age
SELECT MAX(age), MIN(age) FROM users;         -- max and min
SELECT SUM(amount) FROM orders;               -- total amount
SELECT age, COUNT(*) FROM users GROUP BY age; -- group by
SELECT age, COUNT(*) FROM users GROUP BY age HAVING COUNT(*) > 1;
"""
print(aggregate)

print("=== ALTER TABLE ===")
alter = """
ALTER TABLE users ADD COLUMN phone VARCHAR(15);
ALTER TABLE users DROP COLUMN phone;
ALTER TABLE users RENAME COLUMN name TO full_name;
"""
print(alter)
