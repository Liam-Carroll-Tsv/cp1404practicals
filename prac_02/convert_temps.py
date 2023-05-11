import random
CONVERSION_RATE = 9/5


def main():
    menu = """
    Temperature Conversion
    (C)elsius To Fahrenheit
    (F)ahrenheit To Celsius
    (G)enerate Random Input Temps
    (Q)uit
    """
    print(menu)
    choice = input(">>> ").lower()
    temps = read_input_temps()
    while choice != "q":
        if choice == "c":
            celsius_to_fahrenheit(temps)
        elif choice == "f":
            fahrenheit_to_celsius(temps)
        elif choice == "g":
            get_random_temps()
        else:
            print("Invalid Input")
            choice = input(">>> ").lower()
    print("Finished.")
    quit()


def celsius_to_fahrenheit(temps):
    outputs = open("temps_output.txt", "w")
    for i in range(0, len(temps)):
        new_temp = temps[i] * CONVERSION_RATE + 32
        print(f"{round(new_temp, 2)}", file=outputs)
    outputs.close()
    show_output(temps)
    main()


def fahrenheit_to_celsius(temps):
    outputs = open("temps_output.txt", "w")
    for i in range(0, len(temps)):
        new_temp = (temps[i] - 32) / CONVERSION_RATE
        print(f"{round(new_temp, 2)}", file=outputs)
    outputs.close()
    show_output(temps)
    main()


def get_random_temps():
    count = int(input("How Many Temperatures? "))
    inputs = open("temps_input.txt", "w")
    for i in range(0, count):
        temp = random.randint(-200, 200)
        print(temp, file=inputs)
    inputs.close()
    main()


def show_output(temps):
    new_temps = read_output_temps()
    while len(new_temps) < 0:
        print("No Output")
        main()
    for i in range(0, len(temps)):
        print(f"{temps[i]} => {new_temps[i]}", sep="")
    main()


def read_input_temps():
    temps = []
    inputs = open("temps_input.txt")
    for i in inputs:
        temps.append(float(i.strip()))
    return temps


def read_output_temps():
    temps = []
    outputs = open("temps_output.txt")
    for i in outputs:
        temps.append(float(i.strip()))
    return temps


main()
