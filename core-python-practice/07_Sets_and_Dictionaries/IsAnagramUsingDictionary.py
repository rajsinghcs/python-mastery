s1 = "listen"
s2 = "silent"

if(len(s1) != len(s2)):
    print(False)

dict = {}

for char in s1:
    dict[char] = dict.get(char,0)+1

for char in s2:
    dict[char] = dict.get(char,0)-1

for val in dict.values():
    if(val != 0):
        print(False)
        break
else:
    print(True)

