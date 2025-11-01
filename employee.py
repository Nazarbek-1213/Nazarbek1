import psycopg2
from datetime import datetime
from department import *
from country import *
connection=psycopg2.connect(
    dbname="Database_1",
    user="postgres",
    password="Safarov2",
    host="localhost",
    port=5432
)
cursor=connection.cursor()
query="""create table if not exists employee(
employee_id serial primary key,
name varchar(30),
country_id int  references country(country_id),
department_id int  references department(id),
hire_date date,
salary int,
email varchar(40))
"""
cursor.execute(query)
connection.commit()
def add_employee():
    dep_id = add_dep()
    country_id = add_country()

    time = datetime.now().date()
    name = input("employee name: ")
    salary = int(input("salary: "))
    email = input("email: ")

    query = """insert into employee(
        name, country_id, department_id, hire_date, salary, email
    ) values (%s, %s, %s, %s, %s, %s)"""

    cursor.execute(query, (name, country_id, dep_id, time, salary, email))
    connection.commit()

def delete_employee():
    name=input("name: ")
    query="""delete from employee where name=%s"""
    cursor.execute(query,(name,))
    connection.commit()

def list_employee():
    query="""select * from employee"""
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(f"id:{i[0]}, name:{i[1]}, hire date:{i[4]},salary:{i[5]},email:{i[6]}")
    connection.commit()
# # list_country()
def edit_employee():
    old_name=input("old name: ")
    new_name=input("new name: ")
    salary=input("salary: ")
    email=input("email: ")
    query="""update employee set name=%s,salary=%s,email=%s where name=%s """
    cursor.execute(query,(new_name,salary,email ,old_name))
    connection.commit()
def searching():
    country=input("country: ").strip()
    department=input("department:").strip()
    query="""select c.name,d.title, e.name from employee e
     natural join country c 
     natural join department d 
     where name=%s and title=%s 
     group by c.name,d.title,e.name"""
    cursor.execute(query,(country,department))
    data=cursor.fetchall()
    for i in data:
        print(f'name:{i[2]},department:{i[1]},country:{i[0]}')
    connection.commit()

def manager_employee():
    while True:
        menu=input("1.add employee\n2.listing\n3.deleting\n4.editing\n5.choose: ")
        if menu=="1":
            print("#@$@#%$#%$#%$%^")
            add_employee()
        elif menu=="2":
            print("#@$@#%$#%$#%$%^")
            list_employee()
        elif menu=="3":
            print("#@$@#%$#%$#%$%^")
            delete_employee()
        elif menu=="4":
            print("#@$@#%$#%$#%$%^")
            edit_employee()
        else:
            break
def main():
    while True:
        main=input("1.department\n2.country\n3.employee\n4.search\n5.choose:")
        if main=="1":
            manager_dep()
        elif main=="2":
            manager_country()
        elif main=="3":
            manager_employee()
        elif main=="4":
            searching()
        else:
            break
main()

