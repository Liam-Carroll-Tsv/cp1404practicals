items = int(input("Number of items: "))
total = []
while items < 0:
    print("invalid number")
    items = int(input("Number of items: "))
for i in range(0, items):
    price = float(input(f"Price of item {i + 1}: "))
    while price < 0:
        print("invalid price")
        price = float(input(f"Price of item {i + 1}: "))
    total.append(price)
print(f"Total price for 3 items is ${sum(total)}")
