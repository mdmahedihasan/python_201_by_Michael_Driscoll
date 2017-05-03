d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
print(d)

keys = d.keys()
print(keys)

sorted_keys = sorted(keys)
print(sorted_keys)
for key in sorted_keys:
    print(key, d[key])