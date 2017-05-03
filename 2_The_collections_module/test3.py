from collections import Counter


counter = Counter("superfluous")
print(counter)
print(counter["u"])

print(list(counter.elements()))
print(counter.most_common(2))

counter_new = Counter("super")
print(counter.subtract(counter_new))
print(counter)
print(counter_new)