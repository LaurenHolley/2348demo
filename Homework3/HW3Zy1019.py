# Lauren Holley
# 1861058

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = (self.item_price*self.item_quantity)
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total_cost))

    def print_item_description(self):
        print(self.item_name + ": " + self.item_description + ".")

    def item_cost(self):
        return self.item_price * self.item_quantity


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        remove_item = str(input("Enter name of item to remove:\n"))
        i = 0
        for items in self.cart_items:
            if items.item_name == remove_item:
                del self.cart_items[i]
                found = True
                break
            else:
                found = False
            i+=1
        if found == False:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self):
        mod_item = input("Enter the item name:")
        new_q = int(input("\nEnter the new quantity:"))
        for items in self.cart_items:
            if items.item_name == mod_item:
                items.item_quantity = new_q
                found = True
                break
            else:
                found = False
        if found == False:
            print("\nItem not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost

    def print_total(self):
        new_cart = ShoppingCart()
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items:", new_cart.get_num_items_in_cart())
        print()
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            pass
        total_price = 0
        for items in self.cart_items:
            print("{} {} @ ${} = ${}".format(items.item_name, items.item_quantity, items.item_price, (items.item_quantity*items.item_price)))
            total_price += items.item_quantity * items.item_price
        print("\nTotal: ${}".format(total_price))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("\nItem Descriptions")
        for items in self.cart_items:
            print("{}: {}".format(items.item_name, items.item_description))


def print_menu(ShoppingCart):
    c_cart = cart1
    string = ''
    menu = ('\nMENU\n'
        'a - Add item to cart\n'
        'r - Remove item from cart\n'
        'c - Change item quantity\n'
        'i - Output items\' descriptions\n'
        'o - Output shopping cart\n'
        'q - Quit\n')
    user_choice = ''
    while user_choice != 'q':
        string = ''
        print(menu, end='\n')
        user_choice = input('Choose an option:\n')
        while(user_choice != 'a' and user_choice != 'o' and user_choice != 'i' and user_choice != 'r' and user_choice != 'c' and user_choice != 'q'):
            user_choice = input('Choose an option:\n')
        if user_choice == 'a':
            print("ADD ITEM TO CART")
            i_name = str(input("Enter the item name:"))
            i_description = str(input("\nEnter the item description:"))
            i_price = int(input("\nEnter the item price:"))
            i_quantity = int(input("\nEnter the item quantity:\n"))
            c_cart.cart_items.append(ItemToPurchase(i_name, i_price, i_quantity, i_description))

        if user_choice == 'o':
            print("OUTPUT SHOPPING CART")
            c_cart.print_total()

        if user_choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            c_cart.print_descriptions()

        if user_choice == 'r':
            c_cart.remove_item()

        if user_choice == 'c':
            print("CHANGE ITEM QUANTITY")
            c_cart.modify_item()


if __name__ == "__main__":
   c_name = input("Enter customer's name:")
   print()
   today_date = input("Enter today's date:")
   print()
   print()
   print("Customer name: {}".format(c_name))
   print("Today's date: {}".format(today_date))
   cart1 = ShoppingCart(c_name, today_date)
   print_menu(cart1)