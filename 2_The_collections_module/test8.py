from collections import defaultdict

animal = defaultdict(lambda : "Monkey")
animal["sam"] = "Tiger"

print(animal["Nick"])
print(animal)

# x = defaultdict(None)
# print(x["Mike"])