for i in range(1, 21, 2):
    print(i, end=" ")
print()
for i in range(0, 100, 10):
    print(i, end=" ")
print()
for i in range(20, 1, -1):
    print(i, end=" ")
print()
stars = int(input("How many stars: "))
for i in range(0, stars):
    print("*", end=" ")
print()
count = 0
while count < stars:
    count = count + 1
    for i in range(0, count):
        print("*", end="")
    print(sep="")

