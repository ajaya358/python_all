# PostgreSQL - Introduction
# PostgreSQL is a powerful open-source relational database
# Used in almost every Python backend project

print("=== What is PostgreSQL? ===")
concepts = {
    "Database":   "Container that holds all your tables",
    "Table":      "Stores data in rows and columns (like Excel sheet)",
    "Row":        "One record in a table",
    "Column":     "One field/attribute of a record",
    "Primary Key":"Unique ID for each row",
    "Foreign Key":"Links one table to another",
    "Index":      "Speeds up search queries",
    "Schema":     "Namespace to organize tables",
    "Transaction":"Group of queries that run together (all or nothing)",
}
for k, v in concepts.items():
    print(f"  {k:15}: {v}")

print("\n=== PostgreSQL vs Other Databases ===")
comparison = {
    "PostgreSQL": "Relational, ACID, complex queries, open source — best for backend",
    "MySQL":      "Relational, fast reads, widely used in web apps",
    "SQLite":     "File-based, no server, good for dev/testing only",
    "MongoDB":    "NoSQL, stores JSON documents, flexible schema",
    "Redis":      "In-memory key-value, used for caching/sessions",
}
for db, desc in comparison.items():
    print(f"  {db:12}: {desc}")

print("\n=== Install & Connect ===")
print("  Install: https://www.postgresql.org/download/")
print("  pip install psycopg2-binary sqlalchemy")
print()
print("  Connect string: postgresql://username:password@localhost:5432/dbname")
print("  Default port: 5432")
print("  Default user: postgres")

print("\n=== psql CLI Commands ===")
cli = {
    "psql -U postgres":     "Connect as postgres user",
    "\\l":                  "List all databases",
    "\\c dbname":           "Connect to a database",
    "\\dt":                 "List all tables",
    "\\d tablename":        "Describe table structure",
    "\\q":                  "Quit psql",
}
for cmd, desc in cli.items():
    print(f"  {cmd:25}: {desc}")
