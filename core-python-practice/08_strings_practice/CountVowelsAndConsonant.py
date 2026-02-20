text = "engineering"

v_cnt = 0
c_cnt = 0

for char in text:
    if (char =='a' or char =='e' or char =='i' or char =='o' or char =='u'):
        v_cnt+=1
    else:
        c_cnt+=1
print("vowels", v_cnt, " consonant", c_cnt)



#alternative
# text = "engineering"

# vowels = "aeiou"
# vowel_count = 0
# consonant_count = 0

# for char in text:
#     if char in vowels:
#         vowel_count += 1
#     else:
#         consonant_count += 1

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)