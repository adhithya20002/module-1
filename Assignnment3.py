######1)
# Find sum of all elements in a list
list = [1, 2, 3, 4]
print(sum(lst))

###### 2) 
# Remove duplicates from a list
list = [1, 2, 2, 3, 4, 4]
print(list(set(lst)))

######## 3)
# Count frequency of elements in a list
list = [1, 2, 2, 3, 3, 3]
print({x: lst.count(x) for x in lst})

####### )4
# Check if a list is palindrome
lst = [1, 2, 3, 2, 1]
print(lst == lst[::-1])

# 5. Merge two lists and sort
a = [3, 1, 4]
b = [2, 5]
print(sorted(a + b))

# 6. Find common elements in two lists
a = [1, 2, 3]
b = [2, 3, 4]
print(list(set(a) & set(b)))

# 7. Create a tuple and print each element
t = (1, 2, 3)
for x in t:
    print(x)

# 8. Convert list to tuple
lst = [1, 2, 3]
print(tuple(lst))

# 9. Find index of element in tuple
t = (10, 20, 30)
print(t.index(20))

# 10. Check if element exists in tuple
t = (1, 2, 3)
print(2 in t)

# 11. Count number of occurrences in tuple
t = (1, 2, 2, 3)
print(t.count(2))

# 12. Find length of tuple
t = (1, 2, 3, 4)
print(len(t))

# 13. Concatenate two tuples
a = (1, 2)
b = (3, 4)
print(a + b)

# 14. Convert tuple to list and modify
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)

# 15. Create dictionary and print all key-value pairs
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)

# 16. Add, update, delete key-value pair
d = {"a": 1}
d["b"] = 2      # add
d["a"] = 10     # update
del d["b"]      # delete
print(d)

# 17. Find key with maximum value
d = {"a": 5, "b": 8, "c": 3}
print(max(d, key=d.get))

# 18. Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3}
d1.update(d2)
print(d1)

# 19. Count frequency of characters in string
s = "hello"
print({ch: s.count(ch) for ch in s})

# 20. Check if key exists in dictionary
d = {"a": 1, "b": 2}
print("a" in d)

# 21. Create dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
print(dict(zip(keys, values)))
