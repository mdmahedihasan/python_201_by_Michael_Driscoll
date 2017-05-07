import MySQLdb


conn = MySQLdb.connect("localhost", "username", "password", "table_name")
cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name")

row = cursor.fetchone()
print(row)

conn.close()