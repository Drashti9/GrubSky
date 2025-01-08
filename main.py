'''
Test Bench for Grub by Air

This program provides an interactive program to test the behavior of the Order class in
the Grub by Air application.  Commands are entered in response to the menu:

Choose an option:
n - New order
a - Add item to the order
r - Remove item from the order
m - Modify item quantity
p - Print the order
w - Place (write) the order
q - Quit

>

New order creates a new order to work on.  New order will prompt for customer name.

Add item will add an new item to the order by prompting for an item_id and quantity.  Items
are listed in the "available_items.csv" file. Each entry in the file has an item_id, decription and
price.

Remove item will remove an item from the order using an index (zero based) into the list of items to
purchase in the order.

Modify item will modify the quantity of an item in the list of items to purchase.  Prompts for an
index (zero based) and a new quantity.

Print will print the order.

Place order will write the order to a file.  The order will no longer be the current order.  A
new order must be created.

Quit will exit the work bench.

Created on Apr 8, 2020

@author: David Smith, Testing Department
'''

from Order import Order
from csv import reader
from collections import namedtuple
from ItemToPurchase import Item

def get_items():
    ''' Load and return a list the available items found in the file "available_items.csv" '''
    items = {}

    ''' Add code here to load Items from the "available_items.csv" file '''
    with open('available_items.csv', 'r') as file:
        csv_reader = reader(file)

        next(csv_reader)
        for row in csv_reader:
            item_id, description, price_str = row

            try:
                price = float(price_str)
                item = Item(item_id, description, float(price))
                items[item_id] = item
            except ValueError:
                print("Error")
                continue
    return items


if __name__ == '__main__':
    items = get_items()

    order = None

    print('Grub by Air - Test Bench')

    while True:
        try:
            option = ' '
            print()
            print('Choose an option:')
            print('n - New order')

            if order:
                print('a - Add item to the order')
                print('r - Remove item from the order')
                print('m - Modify item quantity')
                print('p - Print the order')
                print('w - Place (write) the order')

            print('q - Quit\n')

            while option not in ['n', 'a', 'm', 'r', 'c', 'p', 'w', 'q']:
                option = input('> ')
                if not order and option not in ['n', 'q']:
                    option = ' '

            if option == 'n':
                print("New Order")
                if order:
                    yesno = input("Current order not placed, do you wish to discard current order y/n:\n")
                    if yesno != 'y':
                        continue
                customer_name = input("Enter customer name:\n")
                order = Order(customer_name)

            elif option == 'a':
                print("Add item")
                item_id = input("Enter the id of an item you wish to purchase:\n")
                if item_id not in items:
                    print(f"Invalid item id")
                    continue

                item = items[item_id]
                quantity = int(input(f"Enter the quantity of {item.description} to purchase:\n"))

                if(quantity ==0):
                    print("Quantity must be greater than zero")

                order.add_item(item, quantity)

            elif option == 'r':
                print('Remove item')
                index = int(input('Enter index of item to remove:\n'))
                order.remove_item(index)

            elif option == 'm':
                print('Modify item quantity')
                index = int(input('Enter index of item to modify:\n'))
                quantity = int(input('Enter the new quantity:\n'))
                order.modify_item(index, quantity)

            elif option == 'p':
                print('Print order')
                order.print_order()

            elif option == 'w':
                print('Place order')
                order.place_order()
                print('Order placed')
                order = None

            elif option == 'q':
                print("Quitting test bench")
                break

        except Exception as e:
            print(e)