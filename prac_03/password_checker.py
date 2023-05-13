MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\t1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input(">>> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input(">>>")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    while len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    for char in password:
        if char in SPECIAL_CHARACTERS:
            count_special = count_special + 1
        if char.isdigit() is True:
            count_digit = count_digit + 1
        if char.islower() is True:
            count_lower = count_lower + 1
        if char.isupper() is True:
            count_upper = count_upper + 1
    while count_lower == 0 or count_upper == 0 or count_digit == 0 or count_special == 0:
        return False
    return True


main()
