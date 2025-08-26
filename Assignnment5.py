# ####1)


# filename = input("Enter the filename: ")
# word = input("Enter the word to search: ")

# try:
#     with open(filename, 'r') as file:
#         for line in file:
#             if word in line:
#                 print(line.strip())
# except FileNotFoundError:
#     print("Error: File not found.")
        
        
        
#######2)



# f = open("data.txt", "a")
# while True:
#     text = input()
#     if text == "exit":
#         break
#     f.write(text + "\n")
# f.close()



# with open("data.txt", "a") as f:
#     while True:
#         text = input("Enter text (type 'exit' to stop): ")
#         if text == "exit":
#             break
#         f.write(text + "\n")
        
        


#######3)

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     print("Result:", num1 / num2)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Please enter valid integers.")
    
    
    
    
#######4))



# class NegativeNumberError(Exception):
#     pass

# try:
#     n = int(input("Enter a number: "))
#     if n < 0:
#         raise NegativeNumberError("Negative number entered")
#     print("Number is:", n)
# except NegativeNumberError as e:
#     print("Error:", e)
# except ValueError:
#     print("Please enter a valid number.")



#####5)


# import math
# radius = int(input("Enter te radius of te circle : "))
# Area=math.pi*radius**2
# circumference=2*math.pi*radius
# print("Area of circle is : " ,Area)
# print("Circumference of circle is : ",circumference)



#####6)


# from datetime import datetime
# import datetime
# print("Current date and time:", datetime.datetime.now())

# d1 = input("Enter first date (DD-MM-YYYY): ")
# d2=input("Enter second date (DD-MM-YYYY)")

# date1 = datetime.datetime.strptime(d1, "%d-%m-%Y")
# date2 = datetime.datetime.strptime(d2, "%d-%m-%Y")

# print("Days between:", abs((date2 - date1).days))




######7)))


# import random
# for i in range(10):
#     roll = random.randint(1, 6)  
#     print("Roll",roll)
    
    

########8)


###########9)

# try:
#     num = int(input("Enter a number: "))
#     print("Square is:", num ** 2)
# except ValueError:
#     print("Error: Please enter a valid number.")


#######10)


# try:
#     age = int(input("Enter your age: "))
#     print("Your age is:", age)
# except ValueError:
#     print("Error: Please enter a valid whole number for age.")



######11)

# while True:
#     try:
#         num = int(input("Enter a valid number: "))
#         print("You entered:", num)
#         break  
#     except ValueError:
#         print("Invalid input. Please enter a number.")

