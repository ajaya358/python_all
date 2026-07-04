# SQL Joins - Combine data from multiple tables
# Most asked topic in backend interviews

print("=== Sample Tables ===")
tables = """
users:                          orders:
id | name  | email              id | user_id | product  | amount
1  | Ajay  | ajay@email.com     1  | 1       | Laptop   | 50000
2  | Ravi  | ravi@email.com     2  | 1       | Phone    | 20000
3  | Priya | priya@email.com    3  | 2       | Tablet   | 15000
4  | Kumar | kumar@email.com    (Kumar has no orders)
"""
print(tables)

print("=== INNER JOIN - only matching rows from both tables ===")
inner = """
SELECT users.name, orders.product, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- Result: Ajay-Laptop, Ajay-Phone, Ravi-Tablet  (Kumar excluded - no orders)
"""
print(inner)

print("=== LEFT JOIN - all rows from left table + matching from right ===")
left = """
SELECT users.name, orders.product, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- Result: Ajay-Laptop, Ajay-Phone, Ravi-Tablet, Kumar-NULL
-- Kumar included with NULL for order columns
"""
print(left)

print("=== RIGHT JOIN - all rows from right table + matching from left ===")
right = """
SELECT users.name, orders.product
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;

-- Result: all orders shown, user NULL if no matching user
"""
print(right)

print("=== FULL OUTER JOIN - all rows from both tables ===")
full = """
SELECT users.name, orders.product
FROM users
FULL OUTER JOIN orders ON users.id = orders.user_id;

-- Result: everything from both tables, NULLs where no match
"""
print(full)

print("=== JOIN with WHERE, ORDER BY, aggregate ===")
advanced = """
-- Total spending per user
SELECT users.name, SUM(orders.amount) AS total_spent
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY users.name
ORDER BY total_spent DESC;

-- Users who spent more than 30000
SELECT users.name, SUM(orders.amount) AS total_spent
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY users.name
HAVING SUM(orders.amount) > 30000;
"""
print(advanced)

print("=== SELF JOIN - join table with itself ===")
self_join = """
-- employees table with manager_id referencing same table
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
"""
print(self_join)
