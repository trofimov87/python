import sqlite3

conn = sqlite3.connect('oknodb.db3')
cursor = conn.cursor()

for row in cursor.execute("SELECT * from proba"):
    print(row)
log = cursor.fetchall()
print(log)