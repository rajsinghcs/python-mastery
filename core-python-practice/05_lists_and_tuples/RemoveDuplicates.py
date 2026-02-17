number = [1,2,20,3,1,4,1,5,5]
unique = []
for i in range(len(number)):
    if(number[i] not in unique):
        unique.append(number[i])

print(unique)
