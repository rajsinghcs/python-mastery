def count_digit(num):
    cnt = 0
    while(num > 0):
        num = num //10
        cnt+=1
    return cnt

print(count_digit(int(input("enter a number "))))