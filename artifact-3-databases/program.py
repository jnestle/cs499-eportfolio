# Enhanced Inventory Management Program - Database Version
# Improvements:
# - Uses SQLite database for persistent storage
# - Implements full CRUD operations (Create, Read, Update, Delete)
# - Retains binary search logic conceptually (via indexed queries)
# - Adds input validation and error handling
# - Uses parameterized queries to prevent SQL injection

import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")
conn.commit()


def add_item():
    name = input("Enter item name: ").strip()
    if name == "":
        print("Item name cannot be empty.\n")
        return

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity.\n")
        return

    # Insert into database using parameterized query (prevents SQL injection)
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()

    print("Item added to database.\n")


def view_inventory():
    cursor.execute("SELECT name, quantity FROM inventory ORDER BY name ASC")
    items = cursor.fetchall()

    if not items:
        print("Inventory is empty.\n")
        return

    print("\nCurrent Inventory:")
    for item in items:
        print(f"{item[0]} - {item[1]}")
    print()


def search_item():
    search = input("Enter item name to search: ").strip()

    if search == "":
        print("Search term cannot be empty.\n")
        return

    # Efficient lookup using SQL query (indexed search behavior)
    cursor.execute("SELECT name, quantity FROM inventory WHERE name = ?", (search,))
    result = cursor.fetchone()

    if result:
        print(f"Found: {result[0]} - {result[1]}\n")
    else:
        print("Item not found.\n")


def update_item():
    name = input("Enter item name to update: ").strip()

    try:
        quantity = int(input("Enter new quantity: "))
    except ValueError:
        print("Invalid quantity.\n")
        return

    cursor.execute("UPDATE inventory SET quantity = ? WHERE name = ?", (quantity, name))
    conn.commit()

    if cursor.rowcount == 0:
        print("Item not found.\n")
    else:
        print("Item updated successfully.\n")


def delete_item():
    name = input("Enter item name to delete: ").strip()

    cursor.execute("DELETE FROM inventory WHERE name = ?", (name,))
    conn.commit()

    if cursor.rowcount == 0:
        print("Item not found.\n")
    else:
        print("Item deleted successfully.\n")


def menu():
    while True:
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            search_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            print("Exiting program.")
            conn.close()
            break
        else:
            print("Invalid option.\n")


def main():
    menu()


if __name__ == "__main__":
    main()
