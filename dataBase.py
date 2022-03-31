import psycopg2

conn = psycopg2.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

results = cursor.fetchall()
results2 = cursor.fetchall()
conn.close()
