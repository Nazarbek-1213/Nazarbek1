# import psycopg2
# from psycopg2 import connect
# import psycopg2
#
#
# class Data_connect:
#     def __init__(self, dbname, user, password, host='localhost', port=5432):
#         self.connection = psycopg2.connect(
#             dbname=,
#             user=user,
#             password="Safarov2",
#             host=host,
#             port=port
#         )
#         self.cursor = self.connection.cursor()
#         self.cursor.close()
#
#     def add_car(self, Model, Title):
#         query = """
#         INSERT INTO cars (model, title)
#         VALUES (%s, %s)
#         """
#         self.cursor.execute(query, (Model, Title))
#         self.connection.commit()
#
#
# My_object = Data_connect('my_database', 'my_user', 'my_password')
#
# while True:
#     menu = input("menu: ")
#     if menu == "1":
#         model = input("model name: ")
#         title = input("title: ")
#         My_object.add_car(model, title)
#
# connecter = DB_connecter()
# connecter.Create_car("Model", "Title")
#
# def Menager_auto_salon():
#     while True:
#         code = input("code: ")
#
#         if code == "1":
#             Model = input("Madel: ")
#             Title = input("Title: ")
#             connecter.Create_car(Model, Title)
#
#
#
# # Menager_auto_salon()
