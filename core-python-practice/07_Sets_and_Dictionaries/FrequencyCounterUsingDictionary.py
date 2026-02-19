numbers = [1, 2, 2, 3, 3, 3]

dict = {}

for i in range(len(numbers)):
    dict[i] = dict.get(i,0)+1

print(dict)