from itertools import combinations


print(list(combinations("WXYZ", 3)))

for item in combinations("WWWW", 3):
    print(''.join(item))