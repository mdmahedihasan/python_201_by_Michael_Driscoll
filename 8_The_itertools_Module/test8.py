my_list = ["foo", "bar"]
numbers = list(range(5))
cmd = ['ls', '/some/dir']
my_list.extend((cmd, numbers))

print(my_list)