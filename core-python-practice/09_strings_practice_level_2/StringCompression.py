text = "aaabbc"

s = ""
cnt = 1

for i in range(1,len(text)):
    if text[i] == text[i-1]:
        cnt+=1
    else:
        s+=text[i-1] + str(cnt)
        cnt=1
s +=text[-1]+ str(cnt)
print(s)
