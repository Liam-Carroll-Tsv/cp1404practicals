def main():
    score = 0
    menu(score)


def menu(score):
    menu = """    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit
    """
    print(menu)
    choice = input(">>> ")
    while choice != "q":
        if choice == "g":
            get_score()
        elif choice == "p":
            print_result(score)
        elif choice == "s":
            show_stars(score)
        else:
            print("Invalid Choice")
            choice = input(">>> ")
    print("Finished.")
    quit()


def get_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Score: "))
    menu(score)


def print_result(score):
    if score > 50:
        if score > 90:
            grade = "Excellent"
        else:
            grade = "Passable"
    else:
        grade = "Bad"
    print(grade)
    menu(score)


def show_stars(score):
    for i in range(0, score):
        print("*", end="")
    print(sep="")
    menu(score)


main()