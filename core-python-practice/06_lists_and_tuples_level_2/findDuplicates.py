list_num = [1,2,3,2,4,5,1]

seen_list = []

for i in range(len(list_num)):
    if(list_num[i] not in seen_list):
        seen_list.append(list_num[i])

print(seen_list)
