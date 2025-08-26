import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="AdiMysql@12345",
  database="Employees")
print(mydb)

mycursor = mydb.cursor()

# # mycursor.execute("CREATE DATABASE Employees")
# mycursor.execute("CREATE TABLE IF NOT EXISTS Employees (id int,name VARCHAR(200),address VARCHAR(200))")

# mycursor = mydb.cursor()
# sql = "INSERT INTO Employees (id,name, address) VALUES (%s, %s,%s)"
# val = ("John", "Kollam")
# mycursor.execute(sql, val)
# values = [
#     ("Arya", "Kochi"),
#     ("Aditya", "Trivandrum"),
#     ("Devika", "Kollam")
# ]
# mycursor.executemany(sql, values)
# mydb.commit()
# print(mycursor.rowcount, "records inserted.")




import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="AdiMysql@12345",
  database="Employees")
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS salesman (salesman_id INT PRIMARY KEY,
                                        name VARCHAR(50),
                                        city VARCHAR(50),
                                        commission DECIMAL(4,2))""")

                 
sql = "INSERT INTO salesman (salesman_id, name, city, commission) VALUES (%s, %s, %s, %s)"
values = [
    (5001, 'James Hoog', 'New York', 0.15),
    (5002, 'Nail Knite', 'Paris', 0.13),
    (5005, 'Pit Alex', 'London', 0.11),
    (5006, 'Mc Lyon', 'Paris', 0.14),
    (5003, 'Lauson Hen', None, 0.12),   
    (5007, 'Paul Adam', 'Rome', 0.13)
]
mycursor.executemany(sql, values)
mydb.commit()
print(mycursor.rowcount, "rows inserted into salesman table.")



mycursor.execute("""CREATE TABLE customer (customer_id INT,
                 cust_name VARCHAR(100),
                 city VARCHAR(100),
                 grade INT,
                 salesman_id INT)""")

sql = "INSERT INTO salesman (salesman_id, name, city, commission) VALUES (%s, %s, %s, %s)"
values = [
  (5001,'James Hoog','New York',0.15),
  (5002,'Nail Knite','Paris',0.13),
  (5005,'Pit Alex' ,'London', 0.11),
  (5006 ,'Mc Lyon' ,'Paris' ,0.14),
  (5003 , 'Lauson Hen', 0.12),
  (5007 ,'Paul Adam' ,'Rome' ,0.13)
]