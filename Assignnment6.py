############
##1)


# matrix=[
#     [1,2,3],
#     [4,5,8],
#     [2,6,4]
# ]
# transpose=[]
# for i in range(len(matrix[0])):
#     row= []
#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     transpose.append(row)
# print("original matrix:",matrix)
# print("transpose:",transpose)



#2)

# lines=[]
# while True:
#     line=input("Enter a line (and press enter to get the output): ")
#     if not line:
#         break
#     lines.append(line.upper())
# for i in lines:
#     print(i)
    
    
    
##3)

# list=[1,2,3]
# print("original list:",list)

# list.append(4)
# print("After append(4):",list)

# list.extend([5,8])
# print("After extend(1,6):",list)

# list.remove(8)
# print("After remove(8):",list)

# print("Pop last element:", list.pop())
# print("List after pop():", list)

# print("Pop element at index 1:", list.pop(1))
# print("List after pop(1):", list)

# print("Index of 3:",list.index(3))

# print("Count of 2:",list.count(2))

# list.sort()
# print("After sort():",list)

# list.reverse()
# print("After reverse():",list)
    
    
##4)

# def read_dict():
#     d={}
#     n=int(input("Number of pairs : "))
#     for i in range(n):
#         key=input("key:")
#         value=int(input("value :"))
#         d[key]=value
#     return d
# dict1=read_dict()
# dict2=read_dict()
# dict1.update(dict2)
# print("Merged dictionary :",dict1)        
        
        
##5)

# d={'a':1,'b':5,'c':7}
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d.get('a'))
# print(d.get('z',0))
# d['c']=3
# print(d)
# d.pop('b')
# print(d)
# d.update({'d':4})
# print(d)
# d.clear()
# print(d)   


##6)

# numbers=[1,2,3,4,5,6]
# total=sum(numbers)
# print("list:",numbers)
# print("sum of elements :",total)


##7)

# n=int(input("Enter an integer"))
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print("Generated dictionary:",d)

##8)

# s=input("Enter a sentence : ")
# letters=sum(c.isalpha() for c in s)
# digits=sum(c.isdigit() for c in s)
# print("Letters :",letters, 'Digits:',digits)

##9)

# from functools import reduce
# numbers =[1,2,3,4,5,6]
# evens =list(filter(lambda x:x%2==0,numbers))
# squares = list(map(lambda x:x*x,evens))
# total =reduce(lambda a,b :a+b,squares)
# print(total)



##10)

# numbers =[1,2,3,4,5,6]
# evens =[x for x in numbers if x%2==0]
# print(evens)



##11)



