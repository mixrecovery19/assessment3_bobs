import json
import os
from datetime import datetime
def save_retail_order(order, filename='retailorders.json'):
        retail_order_data = { # create a dictionary to hold the order data
            "customer_name": order.name,
            "address": order.address,
            "phone_number": order.phone_number,           
            "item_name": order.item_name,
            "quantity": order.quantity,
            "price_per_item": order.price,
            "total_price": order.total_price,
            "discount_rate": order.discount_rate,
            "discount_amount": order.discount_amount,
            "final_price": order.final_price,
            "order_date": datetime.now().isoformat()
        }   
        
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                existing_orders = json.load(file)
        else:
            existing_orders = []

        existing_orders.append(retail_order_data)

        with open(filename, 'w') as file:
            json.dump(existing_orders, file, indent=4)
        print("retail order saved successfully.")
