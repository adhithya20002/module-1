def world():
    print('Hello, Welcome to python!')
world()


# # def greet(name):
# #     print("Hello", name)

# # greet("Adhithya")


# # def add(a,b):
# #     sum=a+b
# #     print("sum",sum)
# # add(10,20)

# # def add(a=25,b=30):
# #     sum=a+b
# #     print("sum",sum)
# # add(2,3)
# # add(2)
# # add()

# # def display_info(first_name,last_name):
# #     print("first_name",first_name)
# #     print("last_name",last_name)
# # display_info(first_name="Adhithya",last_name="M S")

# # def find_sum(*numbers):
# #     result=0
# #     for num in numbers:
# #         result=result+num
# #     print("sum=",result)
# # find_sum(1,2,3)
# # find_sum(4,9)

# ## Anonymous ticket

# x=lambda a:a+10
# print(x(5))

# ##Types)
# #1) map

numbers=[1,2,3,4]
squares=list(map(lambda x:x**2,numbers))
print(squares)

# #2) filter

# number=[1,2,3,4,5,6]
# even=list(filter(lambda x:x%2==0,numbers))
# print(even)

#3) reduce
# from functools import reduce
# total=reduce(lambda x,y :x+y,number)
# print(total)