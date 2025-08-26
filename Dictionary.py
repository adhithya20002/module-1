thisdict={
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":"1964"
    }
print(thisdict)

print(thisdict["Brand"])
x=thisdict.get("Model")
print(x)

x=thisdict.keys()
print(x)

thisdict["color"]="white"
print(x)

x=thisdict.items()
print(x)

thisdict.update({"year":2020})
print(thisdict)

thisdict.pop("Model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["Model"]
print(thisdict)

thisdict.clear()
print(thisdict)


##Loops in dictionaries

for x in thisdict.keys():
    print(x)

for x in thisdict.values():
    print(x)

for x,y in thisdict.items():
    print(x,y)


mydict=dict(thisdict)
print(mydict)


myfamily={
    "child 1":{
        "name":"emil",
        "year":"2004"
    },
    "child 2":{
        "name":"Tobias",
        "Year":"2007"
    },
    "child 3":{
        "name":"linus",
        "year":2011
    }
}
print(myfamily)