# Lauren Holley
# 1861058
# csv module to read the files
import csv
# date module for pastservicedateinventory
from datetime import date as dt
import datetime
#create inventory class with variables for each piece of info
class Inventory:
    def __init__(self):
        self.item_ID = ''
        self.manufacturer = ''
        self.item = ''
        self.damage = ''
        self.price = ''
        self.service_date = ''

# functions to sort items by type, price, ID, and service date for writing to file
def Sort(sub_list):
    sub_list.sort(key=lambda x:x[1])
    return sub_list

def Sort_ID(sub_list):
    sub_list.sort(key=lambda x:x[0])
    return sub_list

def Sort_date(sub_list):
    sub_list.sort(key=lambda x:x[4])
    return sub_list

def Sort_price(sub_list):
    sub_list.sort(key=lambda x:x[4])
    return sub_list

# create empty dictionary to hold values from files
items = {}
# open all 3 files and add/append the values to the dictionary with the
# key being the item ID
with open('ManufacturerList.csv', 'r') as infile:
    item_reader = csv.reader(infile, delimiter=',')
    # sort manufacturer list by item ID
    import operator
    sortedlist = sorted(item_reader, key=lambda x: int(x[0]))
    for row in sortedlist:
        items[row[0]] = row[1:]

with open('PriceList.csv', 'r') as infile:
    price_reader = csv.reader(infile, delimiter=',')
    for row in price_reader:
        items[row[0]].append(row[1])

with open('ServiceDatesList.csv', 'r') as infile:
    date_reader = csv.reader(infile, delimiter=',')
    for row in date_reader:
        items[row[0]].append(row[1])

# create inventory class object
inventory1 = Inventory()
inventory_list = []
# open new file FullInventory to write to
f1 = open('FullInventory.csv', 'w')
# assign all attributes to inventory object and write the line to the file
for key in items:
    inventory1.item_ID = key
    inventory1.manufacturer = items[key][0]
    inventory1.item = items[key][1]
    inventory1.damage = items[key][2]
    inventory1.price = items[key][3]
    inventory1.service_date = items[key][4]
    inventory_list.append([inventory1.item_ID, inventory1.manufacturer,inventory1.item,inventory1.price,inventory1.service_date,inventory1.damage])
# sorted items list and write each element of list to file and close
sorted_items = Sort(inventory_list)
for item in sorted_items:
    for element in item:
        f1.write(str(element)+',')
    f1.write('\n')
f1.close()

# make list to get item types
item_types_list = []
type_list = []
for key in items:
    inventory1.item = items[key][1]
    item_types_list.append(inventory1.item)
    item_types_list = list(set(item_types_list))
# go through list of item types
sorted_types = Sort_ID(inventory_list)

for item in item_types_list:
    # open item Inventory files with item type as name
    f2 = open('{}Inventory.csv'.format(item), 'w')
    for key in items:
        inventory1.item_ID = key
        inventory1.manufacturer = items[key][0]
        inventory1.item = items[key][1]
        inventory1.damage = items[key][2]
        inventory1.price = items[key][3]
        inventory1.service_date = items[key][4]
            # write item to correct item type file
        if inventory1.item == item:
            f2.write("{},{},{},{},{}\n".format(inventory1.item_ID, inventory1.manufacturer,
                            inventory1.price,inventory1.service_date,inventory1.damage))
f2.close()


# open new file PastServiceDateInventory to write to
f3 = open('PastServiceDateInventory.csv', 'w')
today = datetime.datetime.today()
current_date = today.strftime('%m/%d/%Y')
date_list = []
for key in items:
    inventory1.item_ID = key
    inventory1.manufacturer = items[key][0]
    inventory1.item = items[key][1]
    inventory1.damage = items[key][2]
    inventory1.price = items[key][3]
    inventory1.service_date = items[key][4]
    # make list of all dates that are past due
    if datetime.datetime.strptime(current_date, '%m/%d/%Y') > datetime.datetime.strptime(inventory1.service_date,'%m/%d/%Y'):
        date_list.append([inventory1.item_ID, inventory1.manufacturer, inventory1.item, inventory1.price, inventory1.service_date,
        inventory1.damage])
# sort the date list using the sort_date function to have correct order, then write to file
sorted_date = Sort_date(date_list)
for item in sorted_date:
    for element in item:
        f3.write(str(element) + ',')
    f3.write('\n')
f3.close()


# open new file DamagedInventory to write to
f4 = open('DamagedInventory.csv', 'w')
price_list = []
for key in items:
    inventory1.item_ID = key
    inventory1.manufacturer = items[key][0]
    inventory1.item = items[key][1]
    inventory1.damage = items[key][2]
    inventory1.price = items[key][3]
    inventory1.service_date = items[key][4]
    # only add items to list if they are damaged
    if inventory1.damage == 'damaged':
        price_list.append([inventory1.item_ID, inventory1.manufacturer, inventory1.item, inventory1.price, inventory1.service_date])
# sort list of items by price and write to file
sorted_price = Sort_price(price_list)
for item in sorted_price:
    for element in item:
        f4.write(str(element) + ',')
    f4.write('\n')
f4.close()
