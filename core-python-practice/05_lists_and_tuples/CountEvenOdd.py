number = [10, 20, 31, 40, 55]

even_cnt = 0
odd_cnt = 0

for num in number:
    if num % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print("even count-", even_cnt, "odd count-", odd_cnt)
