def main():
    scores = []
    count = int(input("Number of Scores: "))
    while count < 0:
        print("Invalid Number.")
        count = int(input("Number of Scores: "))
    for i in range(0, count):
        score = int(input(f"Score {i + 1}: "))
        while score < 0 or score > 100:
            print("Invalid Score")
            score = int(input("Score: "))
        scores.append(score)
    for i in range(0, len(scores)):
        print(f"{scores[i]} is {get_grade(scores[i])}")


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
