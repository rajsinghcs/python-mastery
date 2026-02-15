num = int(input("Enter a number "))
dig = 0
while(num>0):
    dig+=1
    num = num//10
print(dig)