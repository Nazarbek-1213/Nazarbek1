import psycopg2
connection=psycopg2.connect(
    dbname="Database_1",
    user="postgres",
    password="Safarov2",
    host="localhost",
    port=5432
)
cursor=connection.cursor()
create_table_query="""
CREATE table  IF NOT EXISTS contact_info (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        phone_number VARCHAR(50) )"""

cursor.execute(create_table_query)
connection.commit()

class Contact:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
def add_user():
 name=input("name: ")
 phone_number=input("phone: ")
 contact1=Contact(name,phone_number)
 cursor=connection.cursor()
 query="""
insert into  contact_info 
(name,phone_number)
VALUES(%s,%s)"""
 cursor.execute(query,(contact1.name,contact1.phone_number))
 connection.commit()
def list_ctr():
    query="""
    select * from contact_info"""
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
      print (f"id:{i[0]},name:{i[1]},phone:{i[2]}")
def delete_contact():
    list_ctr()
    a=input("id: ")
    query = "DELETE FROM contact_info WHERE id = %s"
    cursor.execute(query, (a))
    connection.commit()
def manager():
    while True:
        a=input("1.add contact\n2.list\n3.delete\n4.choose: ")
        if a=="1":
            add_user()
        elif a=="2":
            list_ctr()
        elif a=="3":
            delete_contact()
        else:
            break
manager()






