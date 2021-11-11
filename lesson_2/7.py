def my_function(name):
    print(f"hello {name} from my function")


def multi(num):
    return num * num, "foo", "hoo"


my_function("eran")
result = multi(5)
print(result)
