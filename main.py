import psycopg2


conn = psycopg2.connect(
    host='127.0.0.1',
    dbname='store',
    user='postgres',
    password='123456',
    port=5432
)

cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM newtable")
    row = cursor.fetchall()
    print(row)
except Exception as error:
    print("Ошибка ", error)
finally:
    conn.close()
