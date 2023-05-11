CONVERSION_RATE = 9/5


def main():
    menu = """
    Temperature Conversion
    (C)elsius To Fahrenheit
    (F)ahrenheit To Celsius
    (Q)uit
    """
    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            temp = float(input("Temperature °C: "))
            celsius_to_fahrenheit(temp)
        elif choice == "f":
            temp = float(input("Temperature °F: "))
            fahrenheit_to_celsius(temp)
        else:
            print("Invalid Input")
            choice = input(">>> ").lower()
    print("Finished.")
    quit()


def celsius_to_fahrenheit(temp):
    new_temp = temp * CONVERSION_RATE + 32
    print(f"              = {round(new_temp, 2)}°F")
    main()


def fahrenheit_to_celsius(temp):
    new_temp = (temp - 32) / CONVERSION_RATE
    print(f"              = {round(new_temp, 2)}°C")
    main()


main()