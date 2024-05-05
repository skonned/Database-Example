import sqlite3

db = sqlite3.connect("animals.db")
cursor = db.cursor()
sql = "SELECT * FROM animal;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()