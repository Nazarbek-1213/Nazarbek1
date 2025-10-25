import psycopg2
connection=psycopg2.connect(
    dbname="Database_1",
    user="postgres",
    password="Safarov2",
    host="localhost",
    port=5432
)
cursor=connection.cursor()
query="""
create table if not exists car_db(
id serial primary key,
car_name varchar(50),
brend varchar(49),
count int)"""
cursor.execute(query)
connection.commit()
def add_car():
    car_name=input("car_name: ")
    brend=input("brend: ")
    count=input("count: ")
    query="""insert into car_db(car_name,brend,count)
    values(%s,%s,%s)"""
    cursor.execute(query,(car_name,brend,count))
    connection.commit()
def list():
    query="""select * from car_db"""
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(i)
    connection.commit()
def remove_car():
    list()
    a=input("id: ")
    query="delete from car_db where id=%s "
    cursor.execute(query,a)
    connection.commit()
def edit_info():
    list()
    a=input("enter the id: ")
    car_name = input("car_name: ")
    brend = input("brend: ")
    count = input("count: ")
    query="""update car_db
    set car_name=%s,brend=%s,count=%s where id=%s """
    cursor.execute(query,(car_name,brend,count,a))
    connection.commit()
def manager():
    while True:
        a = input("1.add \n2.list\n3.delete\n4.edit\n5.choose: ")
        if a == "1":
            add_car()
        elif a == "2":
            list()
        elif a == "3":
            remove_car()
        elif a=="4":
            edit_info()
        else:
            break
manager()

