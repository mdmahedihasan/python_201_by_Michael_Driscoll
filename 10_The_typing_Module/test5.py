Animal = str


def zoo(animal: Animal, number: int) -> None:
    print("the zoo has %s %s(s)" % (number, animal))


if __name__ == '__main__':
    zoo("monkey", 55)