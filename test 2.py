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
def delete_sms():

