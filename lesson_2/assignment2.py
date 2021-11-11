# A
print("-- A --")
x = 9
y = 30
if x > y:
    print("BIG")
else:
    print("small")

# B
print("\n-- B --")
for i in range(5):
    print(i)

# C
print("\n-- C --")
num = 2
if num == 1:
    print("summer")
elif num == 2:
    print("winter")
elif num == 3:
    print("fall")
elif num == 4:
    print("spring")
else:
    print("Please select a number from 1&2-4")

# D
print("\n-- D --")
print("It will run 10 times and print the number 10")

# E
print("\n-- E --")
age = 39
first_letter_of_lastname = "U"
current_usd_nis_rate = 3.20
trips_abroad = True
apt_num = 50

print("age", age)
print("first letter of last name", first_letter_of_lastname)
print("current USD / NIS rate", current_usd_nis_rate)
print("apt. num", apt_num)
print(current_usd_nis_rate + age)

# F
print("\n-- F --")
phone = input("insert your phone number: ")
print(f"your phone number is: {phone}")

# G
print("\n-- G --")


def printHello():
    print("hello")


def calculate():
    calc = 5 + 3.2
    print(calc)


printHello()
calculate()

# H
print("\n-- H --")


def print_my_name(name):
    print(name)


def divide_by_two(num):
    if num == 0:
        print("0 cannot be divided")
        return

    print(num / 2)


print_my_name("eran")
divide_by_two(5)

# I
print("\n-- I --")


def add(num1, num2):
    return num1 + num2


def concat(str1, str2):
    return f"{str1} {str2}"


print(add(2, 5))
print(concat("foo", "bar"))

# K
print("\n-- K --")


def pyramid_of_asterisks(height):
    result = ""
    for i in range(height):
        string = ""
        for n in range(i + 1):
            string += "*"
        result += string + "\n"
    return result


pyramid = pyramid_of_asterisks(7)
print(pyramid)

# L
print("\n-- L --")


def make_me_a_cross(length):
    if length % 2 == 0:
        print("For a perfect cross please send an odd number\n")
    for i in range(length):
        string = ""
        for n in range(length):
            if n == i or n == (length - 1) - i:
                string += "*"
            else:
                string += " "
        print(string)


make_me_a_cross(7)

# M
print("\n-- M --")


def sum_my_num(num):
    result = 0
    for i in list(str(num)):
        result += int(i)
    return result


result = sum_my_num(46)
print(result)
