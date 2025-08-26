# #ITERATORS

# mytuple=("apple","banana","orange")
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))



##using strings

# mystr="banana"
# myit=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))



##use of iterator in a class(creating an iterator that return number from 1 and it continues)


# class Mynumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass=Mynumber()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



# #Two methods
# ###  @staticmethod

# class Myclass:
#     @staticmethod
#     def greet(name):
#         return f"Hello,{name}!"
# print(Myclass.greet("Alice"))

#### @classmethod


# class Myclass:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Myclass.count+=1
#     @classmethod
#     def get_count(cls):
#         return cls.count
# obj1=Myclass("Alice")
# obj2=Myclass("Bob")
# print(Myclass.get_count())
