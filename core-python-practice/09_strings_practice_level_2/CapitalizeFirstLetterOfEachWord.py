sentence = "python is powerful"
s = ""
for word in sentence.split():
    s+=word.title()+" "
print(s.strip())