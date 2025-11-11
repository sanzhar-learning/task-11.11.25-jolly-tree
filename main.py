#1
for i in range(1,6,1):
    print("*" * i, " " * (6 - i))
print("\n")
#2
for i in range(1,6,1):
    print("* " * i, " " * (6 - i))
print("\n")
#3
for i in range(1,6,1):
    print("* " * (6-i), " " * (i))
print("\n")
#4
for i in range(1,6,1):
    print(" " * (6-i), "*" * (i))
print("\n")
#5
for i in range(1,6,1):
    print(" " * (6 - i), "* " * (i))
print("\n")
#6
for i in range(1, 7):
    print(" " * (6 - i), end="")
    if i == 1:
        print("*")
    elif i == 6:
        print("* " * 6)
    else:
        print("*" + " " * (2 * i - 3) + "*")
print("\n")
#7
for i in range(1,6,1):
    print(" " * (i), "* " * (6-i))
for i in range(2,6,1):
    print(" " * (6 - i), "* " * (i))
print("\n")
#8
for i in range(1,6,1):
    print(" " * (6 - i), "* " * (i))
for i in range(2,6,1):
    print(" " * (i), "* " * (6-i))
print("\n")
#9
for i in range(6, 1, -1):
    print(" " * (6 - i), end="")
    if i == 6:
        print("* " * 6)
    if i == 2:
        print(" *")
    else:
        print("*" + " " * (2 * i - 3) + "*")
#print("     *     ")
for i in range(2, 7):
    print(" " * (6 - i), end="")
    if i == 6:
        print("* " * 6)
    else:
        print("*" + " " * (2 * i - 3) + "*")
print("\n")