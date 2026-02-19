# Invert a Dictionary (Swap Keys and Values)

original = {"a": 1, "b": 2, "c": 3}

invert_dict = {}

for key,val in original.items():
    invert_dict[val] = key

print(invert_dict)
