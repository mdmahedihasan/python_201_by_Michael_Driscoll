import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action="store", help="help text for x")
    group.add_argument('-y', help="help text for y", default=False)

    parser.add_argument('-z', help="help text for z", type=int)
    print(parser.parse_args())


if __name__ == '__main__':
    get_args()