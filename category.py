import psycopg2
from datetime import datetime
connection=psycopg2.connect(
    dbname="Database_1",
    user="postgres",
    password="Safarov2",
    host="localhost",
    port=5432
)
time=datetime.now()
cursor=connection.cursor()
query="""create table if not exists category(
title varchar(30) primary key,
time timestamp)"""
cursor.execute(query)
connection.commit()

def add_category():
    new_category=input("new category: ")
    query="""insert into category(
    title,time)
    values(%s,%s)"""
    cursor.execute(query,(new_category,time))
    connection.commit()
    print("added succesfully")

def list_category():
    query="""select * from category"""
    cursor.execute(query)
    data=cursor.fetchall()
    connection.commit()
    if not data:
        print("***nothing***")
    else:
     for i in data:
         print("here: ")
         print(f'name:{i[0]},sana:{i[1]}')
def searching_category():
   title=input("category name: ")
   query="""select title,time from category where title=%s"""
   cursor.execute(query,(title,))
   connection.commit()
   data=cursor.fetchall()
   if not data:
           print("nothing")
   else:
        for i in data:
           print("here: ")
           print(f'name:{i[0]},sana:{i[1]}')
def edit_category():
    old=input("old title: ")
    title=input("new title: ")
    time=datetime.now()
    query="""update category set title=%s, time=%s where title=%s"""
    cursor.execute(query,(title,time,old))
    connection.commit()
    print("edited succesfully ")
def delete_category():
    category_title=input("title to delete: ")
    time=datetime.now()
    query="""update news set category_title= null,content=null,time_edition=%s
    where category_title=%s 
   """
    cursor.execute(query,(time, category_title))
    connection.commit()
    print("delete succesfully")
def manager_category():
    while True:
     menu=input(' 1.add category\n 2.list category\n 3.searching\n 4.editing\n 5.delete category\n 6.choose: ')
     print("*************")
     if menu=="1":
         add_category()
         print("*************")
     elif menu=="2":
        list_category()
        print("*************")
     elif menu=="3":
        searching_category()
        print("*************")
     elif menu=='4':
        edit_category()
        print("*************")
     elif menu=="5":
        delete_category()
        print("*************")
     else:
        break
# manager_category()






