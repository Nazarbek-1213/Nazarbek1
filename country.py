import psycopg2
connection=psycopg2.connect(
    dbname="Database_1",
    user="postgres",
    password="Safarov2",
    host="localhost",
    port=5432
)
cursor=connection.cursor()
query="""create table if not exists  country(
country_id serial primary key,
title varchar(30),
country_type varchar(30))"""
cursor.execute(query)
connection.commit()
def add_country():
    name = input("country name: ").strip()
    control_type = input("control type: ")
    query = """insert into country(name, country_type)
               values (%s, %s) returning country_id"""
    cursor.execute(query, (name, control_type))
    country_id = cursor.fetchone()[0]
    connection.commit()
    return country_id
# add_country()
def delete_country():
    name=input("name: ")
    query="""delete from country where name=%s"""
    cursor.execute(query,(name,))
    connection.commit()
# delete_country()
def list_country():
    query="""select * from country"""
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(f"id:{i[0]}, title:{i[1]}, control_type:{i[2]}")
    connection.commit()
# list_country()
def edit_country():
    old_name=input("old name: ")
    new_name=input("new name: ")
    control_type=input("type")
    query="""update country set name=%s,country_type=%s where name=%s """
    cursor.execute(query,(new_name,control_type,old_name))
    connection.commit()
# edit_country()
def manager_country():
    while True:
        menu=input("1.add country\n2.listing\n3.deleting\n4.editing\n5.choose: ")
        if menu=="1":
            print("#@$@#%$#%$#%$%^")
            add_country()
        elif menu=="2":
            print("#@$@#%$#%$#%$%^")
            list_country()
        elif menu=="3":
            print("#@$@#%$#%$#%$%^")
            delete_country()
        elif menu=="4":
            print("#@$@#%$#%$#%$%^")
            edit_country()
        else:
            break
# manager_country()