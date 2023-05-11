import random

pop = float(1000)
print("Welcome to the Gopher Population Simulator!")
print(f"Starting Population: {pop}", sep="")
year = int(input("How many years? "))
print()
while year < 0:
    print("Invalid.")
    year = int(input("How many years? "))
for i in range(0, year):
    print(f"Year {i + 1}")
    birth = round(random.uniform(pop * 0.1, pop * 0.2))
    death = round(random.uniform(pop * 0.05, pop * 0.25))
    print(f"{birth} gophers were born. {death} died.")
    pop = round(pop - death + birth)
    print(f"Population: {pop}")
    print()
