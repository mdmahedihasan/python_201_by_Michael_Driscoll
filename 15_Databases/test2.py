import psycopg2


conn = psycopg2.connect(bdname="my_database", user="username")
cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name")
row = cursor.fetchone()

cursor.close()
conn.close()