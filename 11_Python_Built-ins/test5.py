def doubler(x):
    return x * 2


my_list = [1, 2, 3, 4, 5]
for item in map(doubler, my_list):
    print(item)

print(list(map(doubler, my_list)))
print([doubler(x) for x in my_list])