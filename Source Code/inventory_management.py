"""Console-based inventory management system.

Items are stored persistently in inventory.csv using the keys:
    id, name, quantity, price
"""

import csv
import os


INVENTORY_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "inventory.csv"
)


def load_inventory():
    """Load inventory records from CSV, or return an empty list."""
    items = []
    if not os.path.exists(INVENTORY_FILE):
        return items

    with open(INVENTORY_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                items.append({
                    "id": row["id"].strip(),
                    "name": row["name"].strip(),
                    "quantity": int(row["quantity"]),
                    "price": float(row["price"]),
                })
            except (KeyError, TypeError, ValueError):
                continue
    return items


def save_inventory(items):
    """Save all inventory records to the CSV file."""
    with open(INVENTORY_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["id", "name", "quantity", "price"]
        )
        writer.writeheader()
        for item in items:
            writer.writerow({
                "id": item["id"],
                "name": item["name"],
                "quantity": item["quantity"],
                "price": format_number(item["price"]),
            })


def get_next_id(items):
    """Return the next numeric ID based on the highest saved item ID."""
    numeric_ids = []
    for item in items:
        item_id = item["id"].upper()
        if item_id.startswith("I"):
            try:
                numeric_ids.append(int(item_id[1:]))
            except ValueError:
                continue
    return max(numeric_ids, default=100) + 1


def read_non_negative_quantity(
    prompt, allow_blank=False, current=None, retry=True
):
    """Read a non-negative whole-number quantity from the user."""
    while True:
        value = input(prompt).strip()
        if allow_blank and value == "":
            return current
        try:
            quantity = int(value)
            if quantity < 0:
                raise ValueError
            return quantity
        except ValueError:
            if not retry:
                print(
                    "Invalid quantity. Quantity must be a non-negative "
                    "whole number."
                )
                return None
            print(
                "Invalid quantity. Quantity must be a non-negative "
                "whole number."
            )


def read_non_negative_price(prompt, allow_blank=False, current=None):
    """Read a non-negative numeric price from the user."""
    while True:
        value = input(prompt).strip()
        if allow_blank and value == "":
            return current
        try:
            price = float(value)
            if price < 0:
                raise ValueError
            return price
        except ValueError:
            print("Invalid price. Please enter a non-negative number.")


def find_item(items, item_id):
    """Return the item with item_id, or None when it does not exist."""
    for item in items:
        if item["id"].lower() == item_id.strip().lower():
            return item
    return None


def add_item(items, next_id):
    """Add one inventory item and return the next available numeric ID."""
    name = input("Enter item name: ").strip()
    while not name:
        print("Item name cannot be empty.")
        name = input("Enter item name: ").strip()

    quantity = read_non_negative_quantity("Enter quantity: ", retry=False)
    if quantity is None:
        print("Item not added.")
        return next_id

    price = read_non_negative_price("Enter price: ")
    item_id = f"I{next_id}"
    item = {
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price,
    }
    items.append(item)
    save_inventory(items)
    print(
        f"Item added. ID: {item_id} | {name} | "
        f"Qty: {quantity} | Price: {format_number(price)}"
    )
    if quantity < 5:
        print(f"Low stock alert: {name} ({quantity})")
    return next_id + 1


def format_number(value):
    """Format whole numbers without unnecessary trailing zeroes."""
    return f"{value:g}"


def view_items(items):
    """Display all inventory items."""
    if not items:
        print("No items in inventory.")
        return

    print("\nInventory:")
    for item in items:
        print(
            f"{item['id']} | {item['name']} | Qty: {item['quantity']} | "
            f"Price: {format_number(item['price'])}"
        )


def update_item(items):
    """Update an existing item's name, quantity, and price."""
    item_id = input("Enter item ID to update: ").strip()
    item = find_item(items, item_id)
    if item is None:
        print(f"Item ID {item_id} not found.")
        return

    name = input(f"Enter item name [{item['name']}]: ").strip()
    if name:
        item["name"] = name
    item["quantity"] = read_non_negative_quantity(
        f"Enter quantity [{item['quantity']}]: ",
        allow_blank=True,
        current=item["quantity"],
    )
    item["price"] = read_non_negative_price(
        f"Enter price [{item['price']:.2f}]: ",
        allow_blank=True,
        current=item["price"],
    )
    save_inventory(items)
    print("Item updated successfully.")


def search_items(items):
    """Search inventory by item ID or a case-insensitive name fragment."""
    query = input("Enter item ID or name to search: ").strip().lower()
    matches = [
        item for item in items
        if query in item["id"].lower() or query in item["name"].lower()
    ]
    if not matches:
        print("No matching items found.")
        return

    for item in matches:
        print(
            f"{item['id']} | {item['name']} | Qty: {item['quantity']} | "
            f"Price: {format_number(item['price'])}"
        )


def delete_item(items):
    """Delete an item by ID."""
    item_id = input("Enter item ID to delete: ").strip()
    item = find_item(items, item_id)
    if item is None:
        print(f"Item ID {item_id} not found.")
        return

    items.remove(item)
    save_inventory(items)
    print(f"Item '{item['name']}' deleted. Items left: {len(items)}")


def total_stock_value(items):
    """Print and return the total value of all inventory stock."""
    total = 0
    for item in items:
        item_value = item["quantity"] * item["price"]
        total += item_value
        print(f"{item['name']}: {format_number(item_value)}")
    print(f"Total stock value: {format_number(total)}")
    return total


def low_stock_report(items):
    """Display items whose quantity is below five."""
    low_stock_items = [item for item in items if item["quantity"] < 5]
    if not low_stock_items:
        print("No low-stock items.")
        return

    for item in low_stock_items:
        print(
            f"Low stock (below 5): {item['id']} | {item['name']} | "
            f"Qty: {item['quantity']}"
        )


def display_menu():
    """Display the main menu."""
    print(
        "\nInventory Management System\n"
        "1. Add item\n"
        "2. View items\n"
        "3. Update item\n"
        "4. Search item\n"
        "5. Delete item\n"
        "6. Total stock value\n"
        "7. Low-stock report\n"
        "0. Exit"
    )


def main():
    """Run the interactive inventory management menu."""
    items = load_inventory()
    next_id = get_next_id(items)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            next_id = add_item(items, next_id)
        elif choice == "2":
            view_items(items)
        elif choice == "3":
            update_item(items)
        elif choice == "4":
            search_items(items)
        elif choice == "5":
            delete_item(items)
        elif choice == "6":
            total_stock_value(items)
        elif choice == "7":
            low_stock_report(items)
        elif choice == "0":
            print("Exiting inventory management system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
