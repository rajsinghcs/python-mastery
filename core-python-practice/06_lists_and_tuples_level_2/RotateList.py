list_num = [1,2,3,4,5]
k = 2
rotate_list = []
for i in range(len(list_num)-k, len(list_num)):
    rotate_list.append(list_num[i])

for j in range(0,len(list_num)-k):
    rotate_list.append(list_num[j])

print(rotate_list)