tuple_num = (2,3,78,8,65,4)
max = tuple_num[0]
sec_max = tuple_num[0]

for i in range(len(tuple_num)):
    if(tuple_num[i] > max):
        sec_max = max
        max = tuple_num[i]
    elif(tuple_num[i] < max and tuple_num[i] > sec_max):
        sec_max = tuple_num[i]

print(sec_max)