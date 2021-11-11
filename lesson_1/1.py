# string
a = "hello world"

# int
b = 4

# boolean
c = True

# list
d = ["string", 32, True]

# tuple
e = ("moshe", 43, False)

# dictionary
f = {
    "name": "eran",
    "age": 39,
    "isMarried": True,
    "hobbies": ["music", "foo"]
}

print(a)
print(b)
print(c)
print(d)
print(d[1])
d[1] = 48
print(d[1])
print(e)

# cannot do the following line, can't change tuple
# e[2] = True
print(e[2])
print(f["name"])
print(f.keys())
print(f.values())

g = "eran"
h = "uzan"
i = g + " " + h
print(i)
j = 4

# k = g + j will throw error
k = g + str(j)
print(k)

# f (format) will allow us to add vars within a string
lm = f"{g} {h}"
print("lm", lm)

# another option to concat strings
lk = "%s %s" % (g, h)
print("lk", lk)
lt = "eran\n\t \"uzan\""
print("hhh", lt)

if j == 5:
    print("a is 4")
    print("hey again")
print("after if")

number = 7

# 7 to the power of 3
print(number ** 3)

multi_line = """
multi line string
I can start new lines inside the 3 quotes
"""
print(multi_line)
