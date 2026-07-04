# Indexes and Performance - Make queries fast

print("=== What is an Index? ===")
print("  Without index: DB scans every row (slow for large tables)")
print("  With index: DB jumps directly to matching rows (fast)")
print("  Trade-off: faster reads, slightly slower writes, uses disk space\n")

print("=== Create Index ===")
index = """
-- Basic index on one column
CREATE INDEX idx_users_email ON users(email);

-- Index on multiple columns (composite)
CREATE INDEX idx_orders_user_date ON orders(user_id, created);

-- Unique index (also enforces uniqueness)
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);

-- Partial index (only index rows matching condition)
CREATE INDEX idx_active_users ON users(email) WHERE is_active = true;

-- Drop index
DROP INDEX idx_users_email;
"""
print(index)

print("=== EXPLAIN - See how query runs ===")
explain = """
EXPLAIN SELECT * FROM users WHERE email = 'ajay@email.com';
-- Shows: Seq Scan (slow) or Index Scan (fast)

EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'ajay@email.com';
-- Shows actual execution time
"""
print(explain)

print("=== Performance Tips ===")
tips = [
    "Always index columns used in WHERE, JOIN, ORDER BY",
    "Use LIMIT to avoid fetching all rows",
    "Avoid SELECT * — select only needed columns",
    "Use connection pooling (pgBouncer) in production",
    "Use VACUUM to clean up dead rows",
    "Avoid N+1 queries — use JOINs instead of loops",
    "Use prepared statements to prevent SQL injection",
]
for i, tip in enumerate(tips, 1):
    print(f"  {i}. {tip}")

print("\n=== Transactions ===")
transaction = """
-- All or nothing — if one fails, all rollback
BEGIN;
    UPDATE accounts SET balance = balance - 1000 WHERE id = 1;
    UPDATE accounts SET balance = balance + 1000 WHERE id = 2;
COMMIT;

-- If something goes wrong
ROLLBACK;
"""
print(transaction)
