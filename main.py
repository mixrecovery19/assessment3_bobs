"""
Program Overview:
- Demonstrates OOP principles: encapsulation, inheritance, aggregation, polymorphism
- Inventory and customer order system with trade and retail customers
"""
from inventory_manager import InventoryManager# imports InventoryManager class
from handlers.save_trade_order import save_trade_order # imports save_trade_order function
from handlers.save_retail_order import save_retail_order # imports save_retail_order function

class Customer: #sets up the customer class, uses encapsulation, aggregation in the list, it is really only getting ready to display and inheritance polymorphism
    def __init__(self, name, address, phone_number):# sets up the constructor for the customer class
        self.name = name # sets up the name attributes for the customer class object
        self.address = address # sets up the address attributes for the customer class object
        self.phone_number = phone_number # sets up the phone number attributes for the customer class object
        # Initialize an empty list to hold orders
        self.orders = [] # standard list to hold orders for the customer, demonstrating aggregation through creating a list of TradeOrder objects1

    def add_order(self, order): # method to add an order to the customer
        if isinstance(order, TradeOrder): # Check if the order is a TradeOrder
            self.orders.append(order) # Add the order to the customer's orders list

    def display_info(self): # method to display customer information which when called also demonstrates polymorphism
        orders_info = "\n  ".join(order.display_order() for order in self.orders) if self.orders else "No orders placed." # catch to handle if no orders
        return (f"Customer: {self.name}\n" # formatting the customer information
                f"Address: {self.address}\n" 
                f"Phone: {self.phone_number}\n"
                f"Orders:\n  {orders_info}")
    
class TradeCustomer(Customer): # sets up the TradeCustomer class which inherits from Customer uses inheritance, aggregation, and polymorphism
    def __init__(self, name, address, phone_number, email): # sets up the constructor for the TradeCustomer class
        super().__init__(name, address, phone_number) # this calls the constructor of the parent class, in this case Customer
        self.email = email # sets up the email attribute for the TradeCustomer class object
        self.objDiscount = TradeCustomerDiscount()  # this is an instance of the TradeCustomerDiscount class and demonstrates aggregation

    def display_info(self):# method to display TradeCustomer information which when called also demonstrates polymorphism
        orders_info = "\n  ".join(order.display_order() for order in self.orders) if self.orders else "No orders placed." # catch to handle if no orders
        return (f"Online Customer: {self.name}\n" # formatting the TradeCustomer information
                f"Address: {self.address}\n"
                f"Phone: {self.phone_number}\n"
                f"Email: {self.email}\n"
                f"Orders:\n  {orders_info}")
        
    def get_discounted_price(self): # method to get the discounted price
        self.objDiscount.displayTradeDiscount()
        
class TradeCustomerDiscount(): 
    # sets up the TradeCustomerDiscount class, uses encapsulation and is been developed to demonstrate aggregation when it gets used in TradeCustomer & RetailCustomer
    # BUT NOT inheritance or polymorphism
    def __init__(self, trade_discount=25):  # Default to 25 with the use of a default parameter inside the constructor
        self.trade_discount = trade_discount
        self.discount_rate = 25  # Redundant, but keep for clarity

    def displayTradeDiscount(self): # method to display the trade discount
        invoice = f"Trade Discount: {self.trade_discount}%" # formatting the trade discount
        print(invoice)

class TradeOrder(TradeCustomer): # sets up the TradeOrder class which inherits from TradeCustomer, uses encapsulation, inheritance, aggregation, and polymorphism
    def __init__(self, name, address, phone_number, email, inventory_manager, item_name, quantity): # sets up the constructor for the TradeOrder class
        super().__init__(name, address, phone_number, email) # this calls the constructor of the parent class, in this case TradeCustomer, demonstrating inheritance and polymorphism
        self.inventory_manager = inventory_manager  # Aggregation with InventoryManager
        # Initialize order attributes
        self.item_name = item_name
        self.quantity = quantity
        self.price = None
        self.total_price = None
        self.discount_rate = self.objDiscount.trade_discount  # Get discount from TradeCustomerDiscount
        self.discount_amount = 0
        self.final_price = 0
        self.load_item_and_calculate()

    def load_item_and_calculate(self): #method to load item and calculate the price
        inventory = self.inventory_manager.get_inventory()
        for item in inventory:
            if item['item_name'].lower() == self.item_name.lower(): #sets up a case insensitive check for the item name
                if self.quantity > item['quantity']:
                    raise ValueError(f"Only {item['quantity']} units of '{self.item_name}' available.")
                self.price = item['price']  # <<< GETS PRICE FROM JSON
                self.total_price = self.price * self.quantity
                self.discount_amount = self.total_price * (self.discount_rate / 100)
                self.final_price = self.total_price - self.discount_amount
                return
        raise ValueError(f"Item '{self.item_name}' not found in inventory.")

    def display_order(self): # method to display the order information
        return (f"Order for {self.quantity} x {self.item_name} @ ${self.price:.2f} each\n"
                f"Total before discount: ${self.total_price:.2f}\n"
                f"Discount ({self.discount_rate}%): -${self.discount_amount:.2f}\n"
                f"Final price: ${self.final_price:.2f}")

    def display_info(self): # method to display the TradeOrder information
        base_info = super().display_info()
        order_info = self.display_order()
        return f"{base_info}\n{order_info}"
    
class RetailOrder(Customer): # sets up the RetailOrder class which inherits from Customer, uses encapsulation, inheritance, aggregation, and polymorphism
    def __init__(self, name, address, phone_number, inventory_manager, item_name, quantity):
        super().__init__(name, address, phone_number)
        self.inventory_manager = inventory_manager  # Aggregation
        self.item_name = item_name#also referred to as instance variable, sets up the item name attribute for the RetailOrder class object
        self.quantity = quantity
        self.price = None
        self.total_price = None
        self.discount_rate = 0  # No discount for retail orders
        self.discount_amount = 0
        self.final_price = 0
        self.load_item_and_calculate() # calls the method to load item and calculate the price which uses encapsulation, inheritance, aggregation, and polymorphism

    def load_item_and_calculate(self): # creates a method to load item and calculate the price, which uses encapsulation, inheritance, aggregation, and polymorphism
        inventory = self.inventory_manager.get_inventory()
        for item in inventory:
            if item['item_name'].lower() == self.item_name.lower():
                if self.quantity > item['quantity']:
                    raise ValueError(f"Only {item['quantity']} units of '{self.item_name}' available.")
                self.price = item['price']  # <<< GETS PRICE FROM JSON
                self.total_price = self.price * self.quantity
                self.final_price = self.total_price - self.discount_amount
                return
        raise ValueError(f"Item '{self.item_name}' not found in inventory.")

    def display_order(self): # method to display the order information
        return (f"Order for {self.quantity} x {self.item_name} @ ${self.price:.2f} each\n"
                f"Total price: ${self.final_price:.2f}")

    def display_info(self): # method to display the RetailOrder information
        base_info = super().display_info()# uses the display_info method from the parent class Customer which demonstrates inheritance and polymorphism
        order_info = self.display_order() # uses the display_order method from the RetailOrder class which demonstrates encapsulation, inheritance, aggregation, and polymorphism
        return f"{base_info}\n{order_info}"
def main(): # main function to run the program, uses encapsulation, inheritance, aggregation, and polymorphism
        inventory = InventoryManager()
       
        while True:
            print("\n==== 🗂️ MENU ====") # the menu display which is based on basic print commands
            print("1️⃣  Add Inventory")
            print("2️⃣  Add Trade Order")
            print("3️⃣  Add Retail Order")
            print("4️⃣  Exit")

            choice = input("Select an option (1-4): ")

            if choice == "1":
                item_name = input("Enter item name: ")
                try:
                    quantity = int(input("Enter quantity: ")) # converts the input to an integer and catches if the input is not an integer
                    price = float(input("Enter price per item: ")) # converts the input to a float and catches if the input is not a float
                    inventory.add_item(item_name, quantity, price) # adds the item to the inventory using the add_item method from the InventoryManager class
                    print("✅ Inventory added.")
                except ValueError: #inbuilt exception to catch if the input is not a number
                    # If the input is not a number, it will print an error message
                    print("❌ Invalid input. Please enter numeric values for quantity and price.")

            elif choice == "2":
                try:
                    name = input("Customer name: ") # gets the customer name
                    address = input("Address: ")
                    phone_number = input("Phone number: ")
                    email = input("Email: ")
                    inventory_items = inventory.get_inventory()
                    print("\n📦 Available Inventory:")
                    for item in inventory_items:
                        print(f"- {item['item_name']} | Qty: {item['quantity']} | ${item['price']:.2f}")

                    item_name = input("Enter item to order: ")
                    quantity = int(input("Quantity to order: "))
                    order = TradeOrder(name, address, phone_number, email, inventory, item_name, quantity)
                    print("\n🧾 Order Summary:")
                    print(order.display_info())
                    inventory.reduce_stock(item_name, quantity)
                    save_trade_order(order)
                    print("✅ Trade order added successfully.")

                except ValueError as e:
                    print(f"❗ Error: {e}")

            elif choice == "3":
                try:
                    name = input("Customer name: ") # repeats similar steps to the TradeOrder but for RetailOrder
                    address = input("Address: ")
                    phone_number = input("Phone number: ")                    
                    inventory_items = inventory.get_inventory()
                    print("\n📦 Available Inventory:")
                    for item in inventory_items:
                        print(f"- {item['item_name']} | Qty: {item['quantity']} | ${item['price']:.2f}")

                    item_name = input("Enter item to order: ")
                    quantity = int(input("Quantity to order: "))
                    order = RetailOrder(name, address, phone_number, inventory, item_name, quantity)
                    print("\n🧾 Order Summary:")
                    print(order.display_info())
                    inventory.reduce_stock(item_name, quantity)
                    save_retail_order(order)
                    print("✅ Retail order added successfully.")

                except ValueError as e:
                    print(f"❗ Error: {e}")

                
            elif choice == "4":
                print("👋 Exiting program.")
                break

            else:
                print("❌ Invalid choice. Please select 1-4.")
if __name__ == "__main__":
    main()
