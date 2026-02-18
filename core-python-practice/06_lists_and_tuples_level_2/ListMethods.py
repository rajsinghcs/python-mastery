lst = [1, 2, 3, 4]

# append(x) → Add single element at end
lst.append(5)
# [1, 2, 3, 4, 5]


# extend(iterable) → Add multiple elements
lst.extend([6, 7])
# [1, 2, 3, 4, 5, 6, 7]


# insert(index, value) → Insert at specific position
lst.insert(1, 10)
# [1, 10, 2, 3, 4, 5, 6, 7]


# remove(value) → Remove first occurrence of value
lst.remove(2)
# [1, 10, 3, 4, 5, 6, 7]


# pop() → Remove and return last element
lst.pop()
# [1, 10, 3, 4, 5, 6]

# pop(index) → Remove and return element at index
lst.pop(1)
# [1, 3, 4, 5, 6]


# count(value) → Count occurrences
lst.count(3)
# 1


# index(value) → Return index of first occurrence
lst.index(4)
# 2

# index(value, start, end)
lst.index(3,0,5)


# sort() → Sort list in ascending order (in-place)
lst.sort()
# [1, 3, 4, 5, 6]

# sort(reverse=True) → Descending order
lst.sort(reverse=True)
# [6, 5, 4, 3, 1]


# reverse() → Reverse list (in-place)
lst.reverse()
# [1, 3, 4, 5, 6]


# copy() → Create shallow copy
new_lst = lst.copy()
# new_lst = [1, 3, 4, 5, 6]


# clear() → Remove all elements
# lst.clear()
# []



# These are built-in functions
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
print(sorted(lst))