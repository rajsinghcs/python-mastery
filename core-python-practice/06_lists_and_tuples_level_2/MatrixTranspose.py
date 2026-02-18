rows = int(input("Enter row "))
cols = int(input("Enter column "))

matrix = []
print("Enter matrix elements row by row:")
for i in range(rows):
    while(True):
        row = list(map(int,input().split()))
        if len(row) == cols:
            matrix.append(row)
            break
        else:
            print(f"Please enter exactly {cols} elements.")

print(matrix)

