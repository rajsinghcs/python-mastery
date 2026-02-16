def fact_of_num(num):
    i = 1
    fact = 1
    while(i <= num):
        fact *= i
        i += 1
    return fact
print(fact_of_num(int(input("Enter a number "))))