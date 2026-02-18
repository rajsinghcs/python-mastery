list_num = [1,2,3,4,5]
target = 5
# Output: (1,4), (2,3)

for i in range(len(list_num)):
    for j in range(i+1,len(list_num)):
        if(list_num[i] + list_num[j] == target):
            print((list_num[i],list_num[j]), end=" ")

