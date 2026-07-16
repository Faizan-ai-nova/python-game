import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ")

# ❌ Vulnerable
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)

print(cursor.fetchall())
