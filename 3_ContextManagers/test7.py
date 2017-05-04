import sys


path = "text.txt"

with open(path, "w") as f_obj:
    sys.stdout = f_obj
    help(sum)