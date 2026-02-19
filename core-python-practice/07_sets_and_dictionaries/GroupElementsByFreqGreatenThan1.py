numbers = [1, 2, 3, 2, 4, 1, 5]

dict = {}
duplicates = []
for i in numbers:
    dict[i]= dict.get(i,0)+1

for key,val in dict.items():
    if val > 1:
        duplicates.append(key)
 
print(duplicates)