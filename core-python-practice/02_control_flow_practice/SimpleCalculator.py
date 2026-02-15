num1= int(input("Enter a number "))
num2 = int(input("Enter a number "))
operations = input("enter operator (+, -, /, *): ")
if(operations =="+"):
    print(num1+num2)
elif(operations == "-"):
    print(num1-num2)
elif(operations == "/"):
    print(num1/num2)
elif(operations == "*"):
    print(num1*num2)
else:
    print("invalid operator")