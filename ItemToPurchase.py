from collections import namedtuple
import sys

Item = namedtuple('Item', ['item_id', 'description', 'price'])

class ItemToPurchase:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def set_quantity(self, quantity):
        ''' Validates and sets the quantity of the item. '''
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        self.quantity = quantity

    def cost(self):
        return self.quantity * float(self.item.price)

    def print(self, file=sys.stdout):
        price = float(self.item.price)

        if(self.quantity>9 and self.quantity<99):
            print(f" {self.quantity} {self.item.description:<25} @ ${price:5.2f} ea. = ${self.cost():6.2f}", file=file)
        elif(self.quantity==100):
            print(f"{self.quantity} {self.item.description:<25} @ ${price:5.2f} ea. = ${self.cost():6.2f}", file=file)
        else:
            print(f"  {self.quantity} {self.item.description:<25} @ ${price:5.2f} ea. = ${self.cost():6.2f}", file=file)
