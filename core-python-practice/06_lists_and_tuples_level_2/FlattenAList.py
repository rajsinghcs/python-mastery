list_num = [[1,2], [3,4], [5,6]]

flatten_list = []

for i in range(len(list_num)):
    for j in range(len(list_num[i])):
        flatten_list.append(list_num[i][j])

print(flatten_list)