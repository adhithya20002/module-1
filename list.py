thislist=["apple","cherry","banana"]
thislist[0]="orange"
print(thislist)

thislist=["apple","cherry","banana","mango","kiwi","orange"]
thislist[1:3]=["blackcurrent","watermelon"]
print(thislist)

# thislist=["apple","banana","cherry"]
# thislist.insert(2,"kiwi")
# print(thislist)

# ## append
# thislist=["apple","banana","cherry"]
# thislist.append("orange")
# print(thislist)

# thislist=["apple","banana","cherry"]
# tropical=["mango","pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)

thislist=["apple","cherry","banana","mango","kiwi","orange"]
# thislist.remove("orange")
# print(thislist)

# thislist.pop(1)
# # print(thislist)

# thislist.pop()
# print(thislist)

# del thislist
# print(thislist)

# thislist.clear()
# print(thislist)
# for i in range(len(thislist)):
#     print(thislist)


# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if "a"in x]
# print(newlist)


# thislist.sort(reverse=False)
# print(thislist)
# mylist=thislist.copy()
# print(mylist)

mylist=list(thislist)
print(mylist)

list1=["a","b","c"]
list2=[1,2,3]
for x in list2:
    list1.append(x)
    print(list1)