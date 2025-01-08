import sys
from ItemToPurchase import ItemToPurchase

class Order:
    def __init__(self, customer_name="none", order_date="January 1, 2020"):
        self.customer_name = customer_name
        self.order_date = order_date
        self.items_to_purchase = []

    def add_item(self, item, quantity):
        new_item = ItemToPurchase(item, quantity)
        self.items_to_purchase.append(new_item)

    def remove_item(self, index):
        if index < 0 or index >= len(self.items_to_purchase):
            raise IndexError("Invalid index - Item not removed")
        del self.items_to_purchase[index]

    def modify_item(self, index, quantity):
        if index < 0 or index >= len(self.items_to_purchase):
            raise IndexError("Invalid index - Item not modified")
        self.items_to_purchase[index].set_quantity(quantity)

    def get_num_items(self):
        return sum(item.quantity for item in self.items_to_purchase)

    def get_total_cost(self):
        return sum(item.cost() for item in self.items_to_purchase)

    def print_order(self, file=sys.stdout):
        ''' Prints the details of the order in a formatted manner. '''
        print(f"\nORDER - {self.customer_name} {self.order_date}", file=file)
        num_items = self.get_num_items()

        if num_items == 0:
            print("\nORDER IS EMPTY", file=file)
        else:
            print(f"Number of Items: {num_items}\n", file=file)
            for item in self.items_to_purchase:
                item.print(file=file)
            print(f"\n  Total $ {self.get_total_cost():6.2f}", file=file)

    def place_order(self):
        ''' Writes the order details to a file. '''
        if len(self.items_to_purchase) == 0:
            raise RuntimeError("ORDER EMPTY - Order not placed")

        file_name = f"ORDER {self.customer_name} {self.order_date}.txt"
        with open(file_name, 'w') as out_file:
            self.print_order(file=out_file)
