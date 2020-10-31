""""Ricky Tran - 1832920"""

class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(str(self.item_name), str(self.item_quantity), str(self.item_price), str(total)))

if __name__ == "__main__":
    item0 = ItemToPurchase()


    print('Item 1')
    item_name1 = input('Enter the item name:\n')
    item_price1 = int(input('Enter the item price:\n'))
    item_quantity1 = int(input('Enter the item quantity:\n'))

    print()

    print('Item 2')
    item_name2 = input('Enter the item name:\n')
    item_price2 = int(input('Enter the item price:\n'))
    item_quantity2 = int(input('Enter the item quantity:\n'))

    print()

    print('TOTAL COST')
    item1 = ItemToPurchase(item_name1, item_price1, item_quantity1)
    item1.print_item_cost()
    item2 = ItemToPurchase(item_name2, item_price2, item_quantity2)
    item2.print_item_cost()
    total_cost = (item_price1 * item_quantity1) + (item_price2 * item_quantity2)
    print()
    print('Total: ${}'.format(total_cost))