from itertools import cycle


count = 0
for item in cycle(("i love you").split(' ')):
    #if count > 3:
     #   break
    print(item)
    #count += 1