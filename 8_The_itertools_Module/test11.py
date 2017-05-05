from itertools import compress


letters = "ABCDEFGH"
bools = [True, False, True, True, False]

print(list(compress(letters, bools)))