#Mini project: Inventory system

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}, Price: Rs{self.price:.2f}"
    
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed: {item}")
                return
        print(f"Item '{item_name}' not found in inventory.")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item in self.items:
                print(item)

    def total_value(self):
        total = sum(item.quantity * item.price for item in self.items)
        print(f"Total inventory value: Rs{total:.2f}")
        return total
    
def main():
    inventory = Inventory()

    while True:
        print("\nInventory System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Total Value of Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            item = Item(name, quantity, price)
            inventory.add_item(item)

        elif choice == '2':
            item_name = input("Enter item name to remove: ")
            inventory.remove_item(item_name)

        elif choice == '3':
            inventory.display_inventory()

        elif choice == '4':
            inventory.total_value()

        elif choice == '5':
            print("Exiting the inventory system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
