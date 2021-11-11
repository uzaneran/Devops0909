import requests

# we can make lots of excepts for many types of exceptions
# or we can run print(type of e) etc...
try:
    my_variable = int(input("enter first number: "))
    my_other_var = int(input("enter first number: "))
    result = my_variable / my_other_var
    print(result)
except ZeroDivisionError as e:
    print("could not divide by zero")
except ValueError as e:
    print("enter a normal number")
except BaseException as e:
    print(e.args)


# try:
#     requests.get("htpps://github.com")
# except BaseException as e:
#     print("something went wrong: ", e)
#     # or
#     print("args", e.args)
#
# print("hello after mess")


def get_user_age():
    input_from_user = int(input("enter your positive age: "))
    if input_from_user < 0:
        # raise is like throw an exception
        raise ValueError("Age can not be negative")


try:
    get_user_age()
except ValueError as e:
    print(e.args)
