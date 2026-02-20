text = "madam"

left = 0
right =len(text)-1

while(left <= right):
    if text[left] != text[right]:
        print(False)
        break
    else:
        left+=1
        right-=1
print(True)
