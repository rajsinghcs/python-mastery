num = int(input("Enter a number "))

if(num%5==0 and num%11==0):
    print("Divisible by both")
elif(num%5==0):
    print("Divisible by 5")
elif(num%11==0):
    print("Divisible by 11")
else:
    print("Divisile by none")