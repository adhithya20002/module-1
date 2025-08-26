# try:
#     numerator=10
#     aator=0
#     result=numerator/denominator
#     print(result)
# except:
#     print("Error:Denominator cannot be zero")
    
    
#### pyton try with else clause

# try:
#     num=int(input("Enter a number : "))
#     assert num%2==0
# except:
#     print("Not an even number : ")
# else:
#     reciporcal=1/num
#     print(reciporcal)




##### finally


try:
    numerator=10
    denominator=0
    result=numerator/denominator
    print(result)
except:
    print("Error : Denominator cannot be zero")
finally:
    print("This is a final block")