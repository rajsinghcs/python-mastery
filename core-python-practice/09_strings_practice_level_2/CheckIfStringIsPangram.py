text = "the quick brown fox jumps over the lazy dog"
text = text.lower()
s = "abcdefghijklmnopqrstuvwxyz"

for char in s:
    if char not in text:
        print(False)
        break

print(True)