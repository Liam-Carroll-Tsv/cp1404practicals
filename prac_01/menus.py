name = input("Enter name: ")
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
        print(menu)
        choice = input(">>> ").lower()
    elif choice == "g":
        print(f"Goodbye {name}")
        print(menu)
        choice = input(">>> ").lower()
    else:
        print("Invalid choice")
        choice = input(">>> ").lower()
print("Finished.")
quit()

