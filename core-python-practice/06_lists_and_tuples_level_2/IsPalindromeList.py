def isPalindrome(list_num):
    left = 0
    right = len(list_num)-1 
    while(left <= right):
        if(list_num[left] == list_num[right]):
            left+=1
            right-=1
        else:
            return "Not Palindrome"
    return "Palindrome"

list_num = [1, 2, 3, 2, 1]
print(isPalindrome(list_num))
    

