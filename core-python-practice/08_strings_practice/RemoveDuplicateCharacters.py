text = "programming"

set_num = set()
str = ""

for char in text:
    if char not in set_num:
        set_num.add(char)
        str += char

print(str)