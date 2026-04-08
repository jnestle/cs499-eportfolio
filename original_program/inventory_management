

inventory = []

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory.append({"name": name, "quantity": quantity})
    print("Item added.\n")

def view_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.\n")
        return
    for item in inventory:
        print(f"{item['name']} - {item['quantity']}")
    print()

def sort_inventory():
    sorted_list = sorted(inventory, key=lambda x: x["name"])
    for item in sorted_list:
        print(f"{item['name']} - {item['quantity']}")
    print()

def search_item():
    search = input("Enter item name to search: ")
    for item in inventory:
        if item["name"].lower() == search.lower():
            print(f"Found: {item['name']} - {item['quantity']}\n")
            return
    print("Item not found.\n")

def menu():
    while True:
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Sort Inventory")
        print("4. Search Item")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            sort_inventory()
        elif choice == "4":
            search_item()
        elif choice == "5":
            break
        else:
            print("Invalid option\n")

menu()
