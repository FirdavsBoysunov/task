import psycopg2

def connect():

    with psycopg2.connect(database = 'new_db', 
                            user='postgres', 
                            password='112',  
                            host='localhost', 
                            port= 5432) as conn:
        return conn

def select_of_department():
    conn = connect()
    select_all_from_depatment = '''select name as name, id as department_id FROM department;'''
    with conn.cursor() as cursor:
        cursor.execute(select_all_from_depatment)
        data = cursor.fetchall()
    print(data)

def select_of_employee():
    conn = connect()
    select_name_and_id_from_employee = '''SELECT employee_name as employe_name, id as employe_id FROM employee;'''
    with conn.cursor() as cursor:
        cursor.execute(select_name_and_id_from_employee)
        data = cursor.fetchall()
    print(data)
select_of_department()

'''
firdavs boysunov
'''
