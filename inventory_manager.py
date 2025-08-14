import json
import os
from datetime import datetime

class InventoryManager:
    def __init__(self, filename='inventory.json'):
        self.filename = filename
        self.load_inventory()

    def load_inventory(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.inventory = json.load(file)
        else:
            self.inventory = []

    def save_inventory(self):
        with open(self.filename, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, item_name, quantity, price):
        item = {
            "item_id": len(self.inventory) + 1,
            'item_name': item_name,
            'quantity': quantity,
            'price': price,
            'added_on': datetime.now().isoformat()
        }
        self.inventory.append(item)
        self.save_inventory()
        print(f"✅ Added '{item_name}' to inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("ℹ️  No items in inventory.")
            return
        print("\n📦 Current Inventory:")
        for item in self.inventory:
            print(f"- {item['item_name']} | Qty: {item['quantity']} | ${item['price']:.2f} | Added: {item['added_on']}")

    def reduce_stock(self, item_name, quantity):
        for item in self.inventory:
            if item['item_name'] == item_name:
                if item['quantity'] >= quantity:
                    item['quantity'] -= quantity
                    self.save_inventory()
                    print(f"✅ Reduced stock of '{item_name}' by {quantity}.")
                    return
                else:
                    print(f"❗ Not enough stock for '{item_name}'. Available: {item['quantity']}.")
                    return
        print(f"❗ Item '{item_name}' not found in inventory.")

    def get_inventory(self):
            return self.inventory
def main():
    manager = InventoryManager()

    while True:
        print("\n📋 Inventory Management System")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item_name = input("Enter item name: ").strip()
            try:
                quantity = int(input("Enter quantity: ").strip())
                price = float(input("Enter price: ").strip())
                manager.add_item(item_name, quantity, price)
            except ValueError:
                print("❗ Invalid input. Quantity must be an integer, and price must be a number.")
        elif choice == '2':
            manager.display_inventory()
        elif choice == '3':
            print("👋 Exiting the system.")
            break
        else:
            print("❗ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
