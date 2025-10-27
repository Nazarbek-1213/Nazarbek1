import psycopg2
from test import *
from datetime import datetime

connection = psycopg2.connect(
    dbname="Database_1",
    user="postgres",
    password="Safarov2",
    host="localhost",
    port=5432
)
cursor = connection.cursor()

query = """
CREATE TABLE IF NOT EXISTS sms_manager(
    sms_id SERIAL PRIMARY KEY,
    contact_id INT REFERENCES contact_info(contact_id),
    number VARCHAR(50),
    time TIMESTAMP,
    massege TEXT
)
"""
cursor.execute(query)
connection.commit()

def add_sms():
    list_ctr()
    current=datetime.now()
    contact_id=input("choose id to messeging: ")
    query="""select name,phone_number from contact_info
    where contact_id=%s"""
    cursor.execute(query,(contact_id,))
    contact = cursor.fetchone()
    if not contact_id:
        print("not found")
    else:
     massege=input("enter your messege: ")
     number=contact[1]
     query1="""insert into sms_manager
     (contact_id,number,time,massege)
     values(%s,%s,%s,%s)"""
     cursor.execute(query1,(contact_id,number,current,massege))
     connection.commit()
def list_sms():
    query="""select * from sms_manager"""
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(f'sms_id:{i[0]}, contact:{i[2]}, time:{i[3]}, massege:{i[4]}')
def delete_sms():
    list_sms()
    contact_id=input("contact_id to delete: ")
    query="""update sms_manager set massege=NULL where contact_id=%s """
    cursor.execute(query,contact_id)
    connection.commit()
def searching_sms():
       choose=input("1.name\n2.number\n3.which:")
       if choose=="1":
           name=input("name: ")
           if not name:
               print("not sms yet")
           else:
            query = """select c.phone_number,s.time,s.massege from contact_info c
                  inner join sms_manager s on(s.contact_id=c.contact_id) where name=%s"""
            cursor.execute(query, (name,))
            data = cursor.fetchall()
            for i in data:
                if not data:
                    print("not yet")
                else:
                  print(f'number:{i[0]}, time:{i[1]}, massege:{i[2]}')
       elif choose=="2":
           number=input("number: ")
           if not number:
               print("not found")
           else:
                query = """select c.name,s.time,s.massege from contact_info c
                inner join sms_manager s on(s.contact_id=c.contact_id) where number=%s"""
                cursor.execute(query, (number,))
                data = cursor.fetchall()
                for i in data:
                    if not data:
                        print("not yet")
                    else:
                        print(f'name:{i[0]}, time:{i[1]}, massege:{i[2]}')
                        connection.commit()
def editing():
    list_sms()
    a=input("ID: ")
    new_message = input("Enter the new message text: ")
    query="""update  sms_manager set massege=%s where sms_id=%s"""
    cursor.execute(query,(new_message,a))
    connection.commit()

def manager_sms():
   while True:
        a=input("1.sending\n2.list\n3.deleting\n4.searching\n5.edit massege\n6.option: ")
        if a=="1":
            add_sms()
        elif a=="2":
            list_sms()
        elif a=="3":
            delete_sms()
        elif a=="4":
            searching_sms()
        elif a=="5":
            editing()
        else:
            break
def main():
    while True:
        menu=input("1.contacts\n2.sms\n3.option: ")
        if menu=="1":
            manager_contact()
        else:
            manager_sms()
main()



