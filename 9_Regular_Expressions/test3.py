import re


silly_string = "the cat in the hat"
pattern = "the"

match = re.search(pattern, silly_string)
new_match = re.findall(pattern, silly_string)

print(match)
print(new_match)

print(match.group())
