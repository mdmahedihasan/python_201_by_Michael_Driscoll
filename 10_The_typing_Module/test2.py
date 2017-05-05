def process_data(my_list, name):
    if name in my_list:
        return True
    else:
        return False


if __name__ == '__main__':
    my_list = ["mike", "tom", "hom"]
    print(process_data(my_list, "tom"))
    print(process_data(my_list, "xyz"))