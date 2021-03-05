# Lauren Holley
# 1861058
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = (self.item_price*self.item_quantity)
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total_cost))

if __name__ == "__main__":

    item1 = ItemToPurchase()
    print("Item 1")
    item1.item_name = input("Enter the item name:")
    print()
    item1.item_price = int(input("Enter the item price:"))
    print()
    item1.item_quantity = int(input("Enter the item quantity:"))
    print()
    print()
    item2 = ItemToPurchase()
    print("Item 2")
    item2.item_name = input("Enter the item name:")
    print()
    item2.item_price = int(input("Enter the item price:"))
    print()
    item2.item_quantity = int(input("Enter the item quantity:"))

    print()
    print()
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print("Total: $%d" % ((item1.item_price*item1.item_quantity)+(item2.item_price*item2.item_quantity)))
