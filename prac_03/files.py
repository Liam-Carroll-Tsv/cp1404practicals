import random


def main():
    menu = """
    (R)ead Name
    (W)rite Name
    (S)um of Two Numbers
    (A)dd All Numbers
    (Q)uit
    """
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "r":
            read_name()
        if choice == "s":
            add_numbers()
        if choice == "a":
            add_all_numbers()
        if choice == "w":
            write_name()
        else:
            print("Invalid Choice.")
            choice = input(">>> ").lower()
    print("Finished.")
    quit()


def read_name():
    read = open("name.txt", "r")
    for i in read:
        name = i.strip()
        print(f"Your Name is {name}")
    read.close()
    main()


def write_name():
    name = input("What's Your Name? ")
    write = open("name.txt", "w")
    print(name, file=write)
    write.close()
    main()


def add_numbers():
    read = open("numbers.txt", "r")
    numbers = []
    for i in read:
        numbers.append(int(i.strip()))
    a = numbers[random.randint(0, len(numbers) - 1)]
    b = numbers[random.randint(0, len(numbers) - 1)]
    c = a + b
    print(f"{a} + {b} = {c}")
    read.close()
    main()


def add_all_numbers():
    read = open("numbers.txt", "r")
    numbers = []
    for i in read:
        numbers.append(int(i.strip("")))
    print(f"total = {sum(numbers)}")
    read.close()
    main()


main()