dict_num = {1: "one", 2: "two"}

#update iterable
# dictionary
dict_num.update({3: "three", 5: "five"})
print(dict_num)

#list of tuples
dict_num.update([(7, "seven"), (9, "nine")])
print(dict_num)

#tuple of tuples
dict_num.update(((11, "eleven"), (13, "thirteen")))
print(dict_num)

#Using Keyword Arguments
dict_num.update(fifteen="fifteen", seventeen="seventeen")

#copy
temp = dict_num.copy()
#clear
temp.clear()
print("After clear():", temp)

#shallow copy
copy_dict = dict_num.copy()
print("Copy of dictionary:", copy_dict)

#create new dict
new_dict = dict.fromkeys([100, 200, 300], "default")
print("Using fromkeys():", new_dict)

#safe retrival
print("Using get():", dict_num.get(1))              # existing key
print("Using get() with default:", dict_num.get(99, "Not Found"))

#key value pair
print("Using items():", dict_num.items())

#keys
print("Using keys():", dict_num.keys())

#values
print("Using values():", dict_num.values())


#pop() – Remove specific key
removed_value = dict_num.pop(1)
print("After pop(1):", dict_num)
print("Removed value:", removed_value)

# popitem() – Remove last inserted pair
last_item = dict_num.popitem()
print("After popitem():", dict_num)
print("Removed pair:", last_item)


# setdefault() – Get or Insert
dict_num.setdefault(99, "ninety-nine")
print("After setdefault(99):", dict_num)


# If key exists, it does not overwrite
dict_num.setdefault(2, "TWO")
print("After setdefault(2):", dict_num)