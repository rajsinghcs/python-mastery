def reverse_num(num):
    rev = 0
    while(num > 0):
        rev *= 10
        rev += num%10
        num = num//10
    return rev

print(reverse_num(int(input('Enter a number '))))

