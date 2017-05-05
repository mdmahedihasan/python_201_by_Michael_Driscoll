from itertools import chain


my_list = ["foo", "bar"]
numbers = list(range(5))
cmd = ['ls', '/some/dir']

my_new_list = list(chain(my_list, cmd, numbers))
print(my_new_list)

my_new_new_list = my_list + cmd + numbers
print(my_new_new_list)