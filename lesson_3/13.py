def save_name():
    name = input("your name is: ")
    my_file = open("my_names.txt", "a")
    my_file.write(name + "\n")
    my_file.close()


def show_names():
    # with means, only if you succeed then continue and in the end close the file (file descriptor)
    with open("my_names.txt", "r") as my_file:
        for name in my_file.readlines():
            print("current name is: " + name, end='')


try:
    for i in range(4):
        save_name()

    show_names()
except BaseException as e:
    print(e.args)
