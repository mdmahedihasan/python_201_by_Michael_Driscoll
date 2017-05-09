import threading


total = 0
lock = threading.RLock()
# lock = threading.Lock()


def do_something():
    with lock:
        print("lock in do_something")
    print("lock release from do_something")

    return "finished do_something"


def do_something_else():
    with lock:
        print("lock in do_something_else")
    print("lock release from do_something_else")

    return "finished do_something_else"


def main():
    with lock:
        result_one = do_something()
        result_two = do_something_else()

        print(result_one)
        print(result_two)


if __name__ == '__main__':
    main()
    # for i in range(10):
      #  my_thread = threading.Thread(target=main)
       # my_thread.start()