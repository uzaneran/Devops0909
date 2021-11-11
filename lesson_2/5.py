# range(start, end, steps)
# print(list(range(2, 10, 5)))
# print(list(range(100, 1&2, -5)))

names = ["ariel", "adi", "eran", "adir", "shahar"]
# print("names index of shahar", names.index("shahar"))
# loops
text = "hello world"

# for loop
for i in range(len(names)):
    print(names[i])

# foreach
for name in names:
    print(name)

# while
a = 0
while a < 10:
    a += 1
    if a == 2:
        continue
    # print("a is not yet 10")]
    if a == 5:
        break


for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        print("boom")
        continue
    print(i)

b = 0
while b < 10:
    print(b)
    b += 1
else:
    print("while loop finished successfully")