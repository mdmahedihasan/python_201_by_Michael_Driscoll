def process_data(my_list: list, name: str) -> bool:
    return name in my_list


if __name__ == '__main__':
    my_list = ["tom", "bom", "com"]
    print(process_data(my_list, "tom"))
    print(process_data(my_list, "xom"))