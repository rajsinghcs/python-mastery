d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = {}

for key in d1:
    merged[key] = d1[key]

for key in d2:
    merged[key] = d2[key]

print(merged)