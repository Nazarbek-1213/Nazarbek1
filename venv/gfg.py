# import psycopg2
# from datetime import datetime
# connection=psycopg2.connect(
#     dbname="Database_1",
#     user="postgres",
#     password="Safarov2",
#     host="localhost",
#     port=5432
# )
# cursor=connection.cursor()
# query="""create table if not exists  edu_management(
# id serial primary key,
# pasword varchar(40) ,
# name varchar(50),
# surname varchar(50),
# age int,
# course_name varchar(30),
# phone varchar(50),
# time timestamp DEFAULT CURRENT_TIMESTAMP
# )"""
# cursor.execute(query)
# connection.commit()
# class Student:
#     def __init__(self,name,surname,age,major):
#         self.name=name
#         self.surname=surname
#         self.age=age
#         self.major=major
#     def show(self):
#         return f'name:{self.name},surname:{self.surname},age:{self.age},major:{self.major}'
# def add_student():
#     name = input("name: ")
#     surname = input("surname: ")
#     pasword = input("password: ")
#     age = int(input("age: "))
#     phone = input("phone: ")
#     course = input("course name: ")
#
#     insert_query = """
#     INSERT INTO edu_management (pasword, name, surname, age, course_name, phone)
#     VALUES (%s, %s, %s, %s, %s, %s)
#     """
#     cursor.execute(insert_query, (pasword, name, surname, age, course, phone))
#     connection.commit()
#     print("Student successfully added!")
# def list_student():
#     query="""select * from edu_management """
#     data=corspr.fetchall()
#     for i in data:
#         print(f"name:{i[1]},surname:{i[2]},number:{i[5]},age:{i[3]},course:{i[4]}")
# def delete_student():







