sentence = "python is powerful"

words = sentence.split()
rev_words = words[::-1]

result = " ".join(rev_words)
print(result)
