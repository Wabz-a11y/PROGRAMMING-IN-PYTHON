"""
Write a Python program that simulates a simple inventory system.
The program should allow users to add items to the inventory, specify their 
quantities, and update the quantities if the items are already present.

Additionally, users should be able to retrieve information about a specific item in the inventory by entering its name.


"""

inventory = {}

while True:
    print("\n--- Inventory System ---")
    print("1. Add / Update item")
    print("2. View item")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        item = input("Enter item name: ").lower()
        quantity = int(input("Enter quantity: "))

        if item in inventory:
            inventory[item] += quantity
            print(f"{item} updated. New quantity: {inventory[item]}")
        else:
            inventory[item] = quantity
            print(f"{item} added with quantity {quantity}")

    elif choice == "2":
        item = input("Enter item name to view: ").lower()

        if item in inventory:
            print(f"{item}: {inventory[item]} in stock")
        else:
            print("Item not found in inventory.")

    elif choice == "3":
        print("Exiting inventory system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
