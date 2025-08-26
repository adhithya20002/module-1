
##1)

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# student1=student("Adhithya",22)
# student2=student("Devika",25)

# print("student1 Name",student1.name)
# print("student1 Age",student1.age)

# print("student2 Name",student2.name)
# print("student2 Age",student2.age)


##2)

# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         print("Book Title:",self.title)
#         print("Book Author:",self.author)


# b=Book("wings of fire","Dr APJ Abdul Kalam")

##3)

# class student:
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no
#     def display(self):
#         print(f"Name: {self.name} , Roll no : {self.roll_no}")

# student1=student("Aradhya",25)
# student1.display()


##4)

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
# rect1=Rectangle(10,5)
# print(rect1.area())
    
    
##5)

# class Bankaccount():
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#     def withdraw(self,amount):
#         self.balance-=amount
#     def display_balance(self):
#         print(f"owner:{self.owner},balance:{self.balance}")
# acc1=Bankaccount("Aradhya",5000)
# acc1.deposit(10000)
# acc1.withdraw(1500)
# acc1.display_balance()