text = "abc"

substrings = []

for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        substrings.append(text[i:j])

print(substrings)