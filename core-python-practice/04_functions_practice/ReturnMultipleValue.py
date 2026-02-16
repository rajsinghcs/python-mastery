def calculate(a,b):
    return a+b, a-b, a*b, a//b

sum, diff, multiply, div = calculate(5,3)

print("sum", sum)
print("diff", diff)
print("multiply", multiply)
print("div", div)