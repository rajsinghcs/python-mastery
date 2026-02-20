text = "banana"

dict = {}

for char in text:
    dict[char] = dict.get(char,0)+1

print(dict)