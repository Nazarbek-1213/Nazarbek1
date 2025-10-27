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
        contact_id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        phone_number VARCHAR(50) )"""

cursor.execute(create_table_query)
connection.commit()

class Contact:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
def add_user():
 name=input("name: ").lower()
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
    query = "update contact_info  set phone_number = null , name=null  WHERE contact_id = %s"
    cursor.execute(query, (a,))
    connection.commit()

def edit_contact():
    list_ctr()
    a=input("id: ")
    name=input("name: ")
    phone_number=input("phone_number: ")
    query="""update  contact_info
    set name=%s,phone_number=%s where contact_id=%s"""
    cursor.execute(query,(name,phone_number,a))
    connection.commit()
def searching():
   name=input("name: ")
   query="select phone_number from contact_info where name=%s"
   cursor.execute(query,(name,))
   result=cursor.fetchall()
   print(result)
   connection.commit()

def manager_contact():
    while True:
        a=input("1.add contact\n2.list\n3.delete\n4.edit\n5.search\n6.choose: ")
        if a=="1":
            add_user()
        elif a=="2":
            list_ctr()
        elif a=="3":
            delete_contact()
        elif a=="4":
            edit_contact()
        elif a=="5":
            searching()
        else:
            break







