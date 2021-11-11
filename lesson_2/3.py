isTrue = False
a = 5
d = 5
b = 2.5
strOne = "One"
strThree = "Three"

names = ["yaniv", "tom", "liran", "ben"]
# conditions with "if" "elif" "else" "and" and "or"
if a == 2 and strOne == "One" or strThree == "Three":
    print("a is 2")
elif a == 3:
    print("a is 3")
else:
    print("a is not 2")

# not condition
if not a == 5:
    print("a is not 5")

if "shahar" in names:
    print("exists")
