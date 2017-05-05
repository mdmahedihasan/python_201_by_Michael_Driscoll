import re


text = "the ants go marching one by one"
strings = ["the", "one"]

for string in strings:
    match = re.search(string, text)
    if match:
        print('found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text_pos)
        print(text[match.start():match.end()])
    else:
        print('did not find "{}"'.format(string))