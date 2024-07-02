import psycopg2
from typing import Optional
from colorama import Fore


# --------------------------------------------------
def connect():

    with psycopg2.connect(database = 'n48group', 
                            user='postgres', 
                            host='localhost',
                            password='112',   
                            port= 5432) as conn:
        return conn
    

## --------------------------------------------create table
# def create_table():
#         conn = connect()
#         create_table_query = '''
#         create table "user"(
#                         id serial primary key ,
#                         name varchar(100) not null ,
#                         age int ,
#                         email varchar(100) not null ,
#                         is_active bool default false
#         );
#         '''
#         with conn.cursor() as cur:
#              cur.execute(create_table_query)
#              conn.commit()

#         print("succesfully created")

# create_table()        



## ------------------------------------------------------username qolib ketipti
# conn = connect()
# calumn_add_to_user = '''ALTER TABLE "user" add column username varchar(100) not null;'''
# cur= conn.cursor()
# cur.execute(calumn_add_to_user)
# conn.commit()

# -------------------------------------------------------   CLASS

class User:
    def __init__(self, 
                 name:str, 
                 age:int, 
                 is_active:bool,
                 username:Optional[str]=None,
                 email:Optional[str]=None) -> None: 
        self.name=name 
        self.username=username
        self.age=age
        self.email=email
        self.is_active=is_active

    def save(self):
        conn = connect()
        insert_into = '''
        insert into "user"(name, age, is_active, email, username)
        values (%s,%s,%s,%s,%s);
        '''
        data = (self.name, self.age, self.is_active, self.email, self.username)
        with conn.cursor() as cursor:
            cursor.execute(insert_into, data)
            conn.commit()
        
        return "succesfully added data"
    
    @staticmethod
    def get_table():
        conn = connect()
        get_table='''select * from "user";'''
        with conn.cursor() as cursor:
            cursor.execute(get_table)
            data = cursor.fetchall()
        for i in data:
            print(i) 

    def delete_user():
        conn= connect()
        delete_user = '''
        delete from "user" where id = %s;
        '''
        data = input('enter id for delete: ')
        with conn.cursor() as  cursor:
            cursor.execute(delete_user, data)
            conn.commit()
        
        print('delete succesfully')
    
    def update_user():
        conn = connect()

        update_user = '''
            update "user" 
            set name = %s
            where id = 1
            returning *;
        '''
        data= input('name: ')
        with conn.cursor() as cursor:
            cursor.execute(update_user, data)
            conn.commit()
# user = User("Botr", 49, True, "botr@gmail.com", 'botr')


# print(f'{user.save()}\n{get_table()}')
# User.get_table()
# User.delete_user()
# User.delete_user()






    










    # users nomli tabelga Pythonda User classi yozasiz va ushbu classda save(),get_users,
    # get_user,delete_user(),update_user()
    # metodlari bo'lsin va bu metod ishlaganda bazadayam o'zgarishlar hosil bo'lsin