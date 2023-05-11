import random


def main():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Score: "))
    print(f"Grade: {get_grade(score)}")
    score = random.randint(0, 100)
    print(f"Random Score: {score}")
    print(f"Grade: {get_grade(score)}")


def get_grade(score):
    if score > 50:
        if score > 90:
            grade = "Excellent"
        else:
            grade = "Passable"
    else:
        grade = "Bad"
    return grade


main()
