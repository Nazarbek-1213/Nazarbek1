import psycopg2
from datetime import datetime
from category  import *
connection=psycopg2.connect(
    dbname="Database_1",
    user="postgres",
    password="Safarov2",
    host="localhost",
    port=5432
)
cursor=connection.cursor()
time=datetime.now()
query="""create table if not exists news(
category_title varchar(30) references category(title),
content varchar(50),
time_now timestamp,
time_edition timestamp)
"""
cursor.execute(query)
connection.commit()

def add_news():
    add_category()
    news=input("news: ")
    time=datetime.now()
    query="""insert into news(
    content,time_now)
    values(%s,%s)"""
    cursor.execute(query,(news,time))
    connection.commit()

def list_news():
    query="""select * from news"""
    cursor.execute(query)
    data=cursor.fetchall()
    if not data:
        print("nothing")
    else:
        for i in data:
         print(f"category:{i[0]}, content:{i[1]},added_time:{i[2]},edited:{i[3]}")
# add_news()
# list_news()

def searching_content():
    content=input("content: ")
    query="""select from news where content=%s"""
    cursor.execute(query,(content,))
    cursor.commit()
def edit_content():
    while True:
        a=input('1.edit content\n2.edit category name\n3.choose:')
        if a=="1":
         old_content=input("old_content: ")
         new_content_name=input('new content name: ')
         time=datetime.now()
         query="""update news set content=%s,time_edition=%s where content=%s """
         cursor.execute(query,(old_content,time,new_content_name))
        elif a=="2":
            edit_category()
        else:
            break
def manager_news():
   while True:
        a=input("1.add news\n2.list\n3.searching\n4.edit massege\n5.option: ")
        if a=="1":
            add_news()
        elif a=="2":
            list_news()
        elif a=="3":
            searching_content()
        elif a=="4":
            edit_content()
        else:
            break
def main():
    while True:
        menu=input("1.category\n2.news\n3.option: ")
        if menu=="1":
            manager_category()
        else:
            manager_news()
main()



