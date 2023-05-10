def main():
    menu = """    (O)dd Numbers
    (E)ven Numbers
    (S)quared Numbers
    (Q)uit"""
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "o":
            odd()
        elif choice == "e":
            even()
        elif choice == "s":
            squared()
        else:
            print("Invalid Choice")
            choice = input(">>>").lower()
    print("Finished.")
    quit()


def odd():
    x = int(input("Starting Number: "))
    y = int(input("Ending Number: "))
    for i in range(x, y):
        z = i * 2 + 1
        if z < y:
            print(z, end=" ")
    print(sep="")
    main()


def even():
    x = int(input("Starting Number: "))
    y = int(input("Ending Number: "))
    for i in range(x, y):
        z = i * 2
        if z < y:
            print(z, end=" ")
    main()


def squared():
    x = int(input("Starting Number: "))
    y = int(input("Ending Number: "))
    for i in range(x, y):
        z = i ** 2
        if z < y:
            print(z, end=" ")
    main()


main()
