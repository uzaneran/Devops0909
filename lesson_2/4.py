names = ["yaniv", "tom", "liran", "ben"]
other_names = ["yaniv", "tom", "liran", "ben"]
a = 5
d = 5

if a == d:
    print("a equals d")

if a is d:
    print("a is d")

if names is other_names:
    print("names is other names")

print("type of names", type(names))
print("list", list)
print("names == other_names", names == other_names)

my_empty_list = [1]
if 0 < len(my_empty_list) < 5:
    print("hello")
