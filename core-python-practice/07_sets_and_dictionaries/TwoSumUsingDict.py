numbers = [2, 7, 11, 15]
target = 9

dict = {}
for i,j in enumerate(numbers):
    com = target-i
    if com in dict:
        print(dict[com],i)
        break
    dict[j] = i

