list_num = [1,2,4,5,4,3]
target = 4

new_list = []
for i in range(len(list_num)):
    if(list_num[i] != target):
        new_list.append(list_num[i])

print(new_list)