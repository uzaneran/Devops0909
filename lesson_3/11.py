# r = read
# w = write and truncate
# a = append

# open requests from OS the file descriptor
import io

my_file = open("read_my_contents", "r")

# returns a list object
contents = my_file.readlines()

print(contents)
for line in contents:
    # print command by default add a new line "\n" we can tell print that the last char is ''
    # print(line)
    print(line, end='')

# close sending the file descriptor back to the OS
my_file.close()

my_file = open("names.txt", "w")
for i in range(3):
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")

my_file.close()

my_file = open("names.txt", "r")
for name in my_file.readlines():
    print(f"hello {name}", end='')

my_file.close()

try:
    my_file = open("names.txt", "r")
    my_file.write("foo haha")
except FileNotFoundError as e:
    print("file not found")
except io.UnsupportedOperation:
    print("file is not writeable")
my_file.close()
