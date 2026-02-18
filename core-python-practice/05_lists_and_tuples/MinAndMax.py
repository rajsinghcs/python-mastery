number = [190,200,30,40,50]
min = number[0]
max = number[0]
for i in range(len(number)):
    if(number[i]> max):
        max = number[i]
    if(number[i] < min):
        min = number[i]

print("min-", min , "max-", max)