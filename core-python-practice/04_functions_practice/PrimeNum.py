def prime_num(num):
    if(num<2) :
        return 1
    for i in range(2,int(num**0.5)+1):
        if(i%2==0):
            return "Not Prime"
    return False

print(prime_num(int(input("Enter a number "))))

