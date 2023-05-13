try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
# TODO: ValueError check must be added
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")