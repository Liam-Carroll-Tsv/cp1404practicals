TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print()
    print("Electricity bill estimator 2.0")
    print()
    tariff = int(input("Which tariff? 11 or 31: "))
    while tariff != 11 and tariff != 31:
        print("Invalid Tariff")
        tariff = int(input("Which tariff? 11 or 31: "))
    if tariff == 11:
        tariff = TARIFF_11
    elif tariff == 31:
        tariff = TARIFF_31
    use = float(input("Enter daily use in kWh: "))
    while use < 0:
        print("Invalid Input")
        use = float(input("Enter daily use in kWh: "))
    days = int(input("Enter number of billing days: "))
    while use < 0:
        print("Invalid Input")
        days = int(input("Enter number of billing days: "))
    calculator(tariff, use, days)


def calculator(tariff, use, days):
    total = round((use * days * tariff), 2)
    print(f"Estimated bill: ${total}")
    main()


main()

