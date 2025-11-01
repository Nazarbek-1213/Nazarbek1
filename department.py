import psycopg2

connection=psycopg2.connect(
    dbname="Database_1",
    user="postgres",
    password="Safarov2",
    host="localhost",
    port=5432
)
cursor=connection.cursor()
query="""create table if not exists department(
department_id serial  primary key,
title varchar(50))"""
cursor.execute(query)
connection.commit()

def add_dep():
    title = input("dep_title: ")

    query = """insert into department(title) 
               values(%s) returning id"""

    cursor.execute(query, (title,))
    dep_id = cursor.fetchone()[0]
    connection.commit()

    return dep_id

def delete_dep():
    title=input("title: ").strip()
    query="""delete from department where title=%s"""
    cursor.execute(query,(title,))
    connection.commit()
# delete_dep()
def list_dep():
    query="""select * from department"""
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(f"id:{i[0]}, title:{i[1]}")
    connection.commit()
# list_dep()
def edit_dep():
    old_name=input("old name: ")
    new_name=input("new name: ")
    query="""update department set title=%s where title=%s """
    cursor.execute(query,(new_name,old_name))
    connection.commit()
# edit_dep()
def manager_dep():
    while True:
        menu=input("1.add department\n2.listing\n3.deleting\n4.editing\n5.choose: ")
        if menu=="1":
            print("#@$@#%$#%$#%$%^")
            add_dep()
        elif menu=="2":
            print("#@$@#%$#%$#%$%^")
            list_dep()
        elif menu=="3":
            print("#@$@#%$#%$#%$%^")
            delete_dep()
        elif menu=="4":
            print("#@$@#%$#%$#%$%^")
            edit_dep()
        else:
            break
# manager_dep()




