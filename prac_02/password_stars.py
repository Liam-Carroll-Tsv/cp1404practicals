def main():
    password = get_password()
    get_asterisks(password)


def get_asterisks(password):
    for i in range(0, len(password)):
        print("*", end="")


def get_password():
    password = input("Password: ")
    length = 10
    while len(password) > length:
        print("Must fit in Character Limit.")
        password = input("Password: ")
    return password


main()
