from contextlib import suppress


with suppress(FileNotFoundError):
    with open("no_file") as f_obj:
        for line in f_obj:
            print(line)