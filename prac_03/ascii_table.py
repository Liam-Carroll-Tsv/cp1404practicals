LOWER = 33
UPPER = 127
a = input("Enter a character: ")
b = ord(a)
print(f"The ASCII code for {a} is {b}")
c = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
print(f"The character for 100 is {chr(c)}")
while c > UPPER or c < LOWER:
    print("Invalid Number")
    c = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
for i in range(33, 127):
    print(f"{i:5}    {chr(i)}")
