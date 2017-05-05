import re


text = "The ants go marching one by one"
strings = ["The", "one"]

for string in strings:
    regex = re.compile(string)
    print(regex)
    match = re.search(regex, text)
    if match:
        print('found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('did not find "{}"'.format(string))