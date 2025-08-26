thisset={"apple","banana",False,True,1,2}
print(thisset)

thisset={"apple","banana",False,True,1,2,0}
print(thisset)

thisset={"apple","banana","cherry"}
thisset.add("kiwi")
print(thisset)

thisset={"apple","banana","cherry"}
tropical={"pineqapple","mango","papaya"}
thisset.update(tropical)
print(thisset)

thisset={"apple","banana","cherry"}
thisset.remove("apple")
print(thisset)

thisset={"apple","banana","cherry"}
x=thisset.pop()
print(x)
print(thisset)


thisset={"apple","banana","cherry"}
thisset.clear()
print(thisset)

thisset={"apple","banana","cherry"}
del thisset
print(thisset)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1|set2
print(set3)
set4=set1&set2
print(set4)
set5=set1-set2
print(set5)
set6=set1^set2
print(set6)

x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.isdisjoint(y)
print(z)