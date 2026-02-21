strs = ["flower", "flow", "flight"]
s = strs[0]
for word in strs[1:]:
    while not word.startswith(s):
        s = s[:-1]
print(s)