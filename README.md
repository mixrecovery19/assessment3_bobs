Kind of cool Inventory orders program. 

This is a very simple but effective inventory manager program. With both trade and retail customers written as a TAFE assessment to demonstrate knowledge of
***Polymorphism***
***Inheritance***
***Aggregation***
***Encapsulation***

📚 Object-Oriented Programming Concepts Demonstrated

This project is designed as an Inventory and Customer Order Management System that showcases multiple OOP principles in Python:

1. Encapsulation

Encapsulation is shown through the use of classes with attributes and methods that keep related data and functionality bundled together.
For example:

The TradeOrder and RetailOrder classes store all order-related data (item_name, quantity, price, etc.) and have methods like load_item_and_calculate() that operate only on that data.

Attributes like self.price or self.discount_rate are maintained within the object, shielding direct manipulation from the outside.

2. Inheritance

Inheritance allows classes to reuse and extend existing functionality:

TradeCustomer inherits from Customer.

TradeOrder inherits from TradeCustomer.

RetailOrder inherits from Customer.
This eliminates code duplication and allows specialized classes to build upon general-purpose ones.

3. Aggregation

Aggregation is demonstrated by including instances of other classes as attributes:

TradeCustomer contains an instance of TradeCustomerDiscount.

TradeOrder and RetailOrder both hold a reference to InventoryManager for stock operations.

The Customer class holds a list of orders (self.orders), which are themselves objects of other classes.

4. Polymorphism

Polymorphism appears where the same method name behaves differently depending on the object:

The display_info() method is implemented in Customer, TradeCustomer, TradeOrder, and RetailOrder with tailored output for each type.

Both TradeOrder and RetailOrder have display_order() methods, but each returns a format appropriate to that order type.

5. Composition of Functionality

Beyond pure aggregation, the system demonstrates composition by combining classes and functions from multiple modules:

Functions like save_trade_order() and save_retail_order() are integrated into the workflow but live in separate handler modules.

6. Error Handling & Validation

The program makes use of exception handling (try/except) to manage invalid input, missing inventory items, and insufficient stock. This is an important real-world coding practice to ensure robustness.

7. Separation of Concerns

Different files/modules handle distinct responsibilities:

inventory_manager.py manages stock.

handlers/ folder handles saving orders.

Main script orchestrates input, processing, and output.
