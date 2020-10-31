""""Ricky Tran - 1832920"""

class ItemToPurchase:
    def __init__(self, item_name='none', item_description='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity


    def print_item_description(self):
        print('{}: {}'.format(str(self.item_name, str(self.item_description))))

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(str(self.item_name), str(self.item_quantity), str(self.item_price), str(total)))

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, remove):
        i = 0
        itm = self.cart_items[:]
        l = len(itm)
        ll = int(l)
        for i in range(ll):
            it = itm[i]
            if it.item_name == remove:
                del self.cart_items[i]
                i += 1
        if i == 0:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, modify, nq):
        m = str(modify)
        nqi = int(nq)
        i = 0
        itm = self.cart_items[:]
        l = len(itm)
        ll = int(l)
        for i in range(ll):
            it = itm[i]
            if it.item_name == m:
                it.item_quantity = nqi
                i += 1
        if i == (ll-1):
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num_items_in_cart = 0
        for item in self.cart_items:
            num_items_in_cart = num_items_in_cart + item.item_quantity
        return num_items_in_cart

    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = item.item_quantity * item.item_price
            total_cost += cost
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CHART IS EMPTY')
        else:
            print(total_cost)

    def print_description(self):
        new = ShoppingCart()
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print()
        print('Item Descriptions')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))

    def out_cart(self):
        new = ShoppingCart()
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', new.get_num_items_in_cart(), end='\n')
        print()
        if new.get_num_items_in_cart() != 0:
            for item in self.cart_items:
                print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity, item.item_price, (item.item_quantity * item.item_price)))
            print()
            btotal = self.get_cost_of_cart()
            print('Total: ${}'.format(btotal), end='\n')
        else:
            print('SHOPPING CART IS EMPTY')
            print()
            print('Total: $0')


def print_menu(ShoppingCart):
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')

    print(menu, end='\n')


if __name__ == "__main__":
    customer_name = str(input("Enter customer's name:\n"))
    current_date = str(input("Enter today's date:\n"))
    print()
    print('Customer name:', customer_name, end='\n')
    print("Today's date:", current_date, end='\n')

    ncart = ShoppingCart(customer_name, current_date)

    print_menu(ncart)
    option = ''
    while (option != 'q'):
        option = input('Choose an option:\n')
        if option == 'o':
            ncart.out_cart()
            print_menu(ncart)
        elif option == 'a':
            print('ADD ITEM TO CART')
            item_name1 = input('Enter the item name:\n')
            item_description1 = input('Enter the item description:\n')
            item_price1 = int(input('Enter the item price:\n'))
            item_quantity1 = int(input('Enter the item quantity:'))
            print()
            item1 = ItemToPurchase(item_name1, item_description1, item_price1, item_quantity1)
            ncart.add_item(item1)
            print_menu(ncart)
        elif option == 'r':
            print('REMOVE ITEM FROM CART')
            item_remove = input('Enter name of item to remove:\n')
            ncart.remove_item(item_remove)
            print_menu(ncart)
        elif option == 'c':
            print('CHANGE ITEM QUANTITY')
            cname = input('Enter the item name:\n')
            newq = input('Enter the new quantity:\n')
            ncart.modify_item(cname, newq)
            print_menu(ncart)
        elif option == 'i':
            ncart.print_description()
            print_menu(ncart)
