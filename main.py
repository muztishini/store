import psycopg2


conn = psycopg2.connect(
    host='127.0.0.1',
    dbname='store',
    user='postgres',
    password='123456',
    port=5432
)

cursor = conn.cursor()

num_list = input("Введите список заказов, разделенных пробелом: ").split()

try:
    # cursor.execute('insert into product (name) values ('ноутбук'),('монитор'),('телефон'),('системный блок'),('часы'),('микрофон')')
    # conn.commit() 
    
    # cursor.execute('insert into "order" (num_order, product_id, quantity) values (10, 1, 2), (10, 3, 1), (10, 6, 1)')
    # cursor.execute('insert into "order" (num_order, product_id, quantity) values (11, 2, 3)')
    # cursor.execute('insert into "order" (num_order, product_id, quantity) values (14, 1, 3), (14, 4, 4)')
    # cursor.execute('insert into "order" (num_order, product_id, quantity) values (15, 5, 1)')
    # conn.commit()
    
    # cursor.execute("insert into rack (name, product_id, quantity) values ('A', 1, 100), ('A', 2, 100)")
    # cursor.execute("insert into rack (name, product_id, quantity) values ('B', 3, 100)")
    # cursor.execute("insert into rack (name, product_id, quantity) values ('C', 4, 100), ('C', 5, 100), ('C', 6, 100)")
    # cursor.execute("insert into rack (name, product_id, quantity) values ('D', 3, 100)")
    # cursor.execute("insert into rack (name, product_id, quantity) values ('E', 3, 100)")
    # cursor.execute("insert into rack (name, product_id, quantity) values ('F', 5, 100)")
    # conn.commit()
       
    # cursor.execute('SELECT * FROM rack')
    # row = cursor.fetchall()
    # print(row)
    num_list = list(map(int, num_list))
    print("Страница сборки заказов: ", num_list)
    for i in num_list:
        cursor.execute(f'SELECT num_order, product_id, quantity FROM "order" WHERE num_order={i}')
        row = cursor.fetchall()
        print(row)
           
except Exception as error:
    print("Ошибка ", error)
finally:
    conn.close()
