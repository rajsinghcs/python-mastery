set_num = {2,4,6,8,10}

#add
set_num.add(1)
print(set_num)

#update
set_num.update({3, 5, 7})
set_num.update([9, 11, 13])
print(set_num)

#remove
set_num.remove(1)
print(set_num)

#discard(remove element, give no error if not present)
set_num.discard(1)
print(set_num)


# pop (remove and return)
set_num.pop()
print(set_num)

#clear
set_num.clear()
print(set_num)


#Methods That Return New Sets
a= {2,4,6,8,10}
b = {1,3,5,7,9}

#union
print(a.union(b))
print(a|b)

#intersection
print(a.intersection(b))
print(a&b)

#difference
print(a.difference(b))
print(a-b)

#symmetric difference
print(a.symmetric_difference(b))
print(a^b)


#Modify Original Set
a = {1,2,4,6,8,10}
b = {1,2,5,7,9}

print(a.intersection_update(b))
print(a.difference_update(b))
print(a.symmetric_difference_update(b))


#Comparison / Boolean Methods


#issubset
print(a.issubset(b))
print(a <= b)

#issuperset
print(a.issuperset(b))
print(a <= b)

#isdisjoint
print(a.isdisjoint(b))


#Built-in Functions Commonly Used With Sets

print(len(a))
min(a)
print(max(a))
print(sum(a))
print(sorted(a))


#Special Set Type

#frozenset(immutable)
fs = frozenset([1, 2, 3])