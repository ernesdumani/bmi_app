import sqlite3

# Connect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Create a table named 'employees'
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
''')
connection.commit()

# Insert a new employee
cursor.execute('''
INSERT INTO employees (name, position, department, salary)
VALUES (?, ?, ?, ?)
''', ('John Doe', 'Software Engineer', 'IT', 2000))
connection.commit()

# Select and print all employees
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
UPDATE employees
SET salary=?
WHERE name=?
''', (3000, 'John Doe'))

connection.commit()

cursor.execute('''
DELETE FROM employees
WHERE name=?
''', ('John Doe'))

connection.commit()

cursor.close()
connection.close()