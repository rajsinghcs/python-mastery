text = "aabbcdde"

dict = {}

for char in text:
    dict[char]= dict.get(char,0)+1

for key,val in dict.items():
    if(val == 1):
        print(key)
        break
else: 
    print("not found")
