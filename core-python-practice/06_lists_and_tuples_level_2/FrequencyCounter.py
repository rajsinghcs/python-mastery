list_num = [1, 2, 2, 3, 1, 4, 2]

freq = {}

for i in list_num:
    freq[i] = freq.get(i, 0) + 1

print(freq)
