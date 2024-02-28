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
       
    num_list = list(map(int, num_list))  
    print("Страница сборки заказов: ", num_list)
    
    cursor.execute(f"SELECT name, product_id FROM rack WHERE name='A' OR name='B' OR name='C'")
    racks = cursor.fetchall()    
    result_dict = {}
    for key, value in racks:
        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]
    result_list = [(key, value) for key, value in result_dict.items()]   
    for item in result_list:
        rack_name = item[0]
        print(f"===Стеллаж {rack_name}")
        for prod in item[1]:
            cursor.execute(f'SELECT num_order, product_id, quantity FROM "order" WHERE product_id={prod}')
            row = cursor.fetchall()
            for r in row:
                if r[0] in num_list:
                    cursor.execute(f'SELECT name FROM product WHERE id={r[1]}')
                    name_prod = cursor.fetchone()[0]
                    print(f"{name_prod} (id={r[1]})")
                    print(f"заказ {r[0]}, {r[2]} шт")                
                    cursor.execute(f"SELECT name FROM rack WHERE product_id={r[1]} AND name!='A' AND name!='B' AND name!='C'")
                    dop_racks = cursor.fetchall()
                    if dop_racks != []:
                        dr = ""
                        for i in dop_racks:
                            dr += f"{i[0]},"                    
                        print(f"доп стеллаж: {dr}")
                    print(" ")
                
except Exception as error:
    print("Ошибка ", error)
finally:
    conn.close()
