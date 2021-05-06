# Lauren Holley
# 1861058
import csv
from datetime import date as dt
import datetime
import operator
import copy
def get_key(val):
    for key, value in mi_dict.items():
        if val == value:
            return key

def get_copy_key(val):
    for key, value in copy_dict.items():
        if val == value:
            return key
def lookup(dct,*args):
    for i in args:
        dct = {key: value for key, value in dct.items() if i in value}
    return dict

class Inventory:
    def __init__(self):
        self.item_ID = ''
        self.manufacturer = ''
        self.item = ''
        self.damage = ''
        self.price = ''
        self.service_date = ''

items = {}
# open all 3 files and add/append the values to the dictionary with the
# key being the item ID
with open('ManufacturerList.csv', 'r') as infile:
    item_reader = csv.reader(infile, delimiter=',')
    for row in item_reader:
        items[row[0]] = row[1:]

with open('PriceList.csv', 'r') as infile:
    price_reader = csv.reader(infile, delimiter=',')
    for row in price_reader:
        items[row[0]].append(row[1])

with open('ServiceDatesList.csv', 'r') as infile:
    date_reader = csv.reader(infile, delimiter=',')
    for row in date_reader:
        items[row[0]].append(row[1])

inventory1 = Inventory()
inventory_list = []
# make lists for item and manufacturer to check user input against
mname = []
item_type = []
# dictionary to check if combo of manufacturer and item exist
mi_dict = {}
# price with ID as key
price_dict = {}
# damage indicator with ID as key
damage_dict = {}
# service dates with ID as key
date_dict = {}
today = datetime.datetime.today()
current_date = today.strftime('%m/%d/%Y')
# go through and add each element to inventory1 class
for key in items:
    inventory1.item_ID = key
    inventory1.manufacturer = items[key][0]
    inventory1.item = items[key][1]
    inventory1.damage = items[key][2]
    inventory1.price = items[key][3]
    inventory1.service_date = items[key][4]
    # only add to inventory is not damaged/past service date
    if inventory1.damage == '':
        # print only if today's date isn't past the service date
        if datetime.datetime.strptime(current_date, '%m/%d/%Y') < datetime.datetime.strptime(inventory1.service_date,'%m/%d/%Y'):
            inventory_list.append([inventory1.item_ID, inventory1.manufacturer,inventory1.item,
            inventory1.price,inventory1.service_date,inventory1.damage])
            # populating the individual dictionaries with necessary info
            mname.append(inventory1.manufacturer)
            item_type.append(inventory1.item)
            mi_dict[key] = (inventory1.manufacturer.lower()+" "+inventory1.item.lower())
            price_dict[key] = inventory1.price
            damage_dict[key] = inventory1.damage
            date_dict[key] = inventory1.service_date
# sort by highest price
sorted_price_dict = dict(sorted(price_dict.items(), key = operator.itemgetter(1), reverse=True))

# prompt user for item info
user_input = input("Enter manufacturer and item type")
# loop until user want to quit
while user_input != 'q':
    # split input to determine if there are extra words
    search_terms = user_input.split(" ")
    # ignore words like 'nice'
    if len(search_terms) > 2:
        search_terms.pop(0)
    user_input =" ".join(search_terms)
    # determine if user input is in inventory
    if user_input.lower() in mi_dict.values():
        ID_item = get_key(user_input)
        print("Your item is: {}, {}, {}".format(get_key(user_input.lower()),user_input, price_dict.get(ID_item)))
        # get item type
        rec_item = search_terms[-1]
        # delete item user asked for to see what is left in inventory
        del mi_dict[get_key(user_input)]
        values = []
        copy_dict = mi_dict.copy()
        for value in list(copy_dict.values()):
            if rec_item in value:
                values.append(str(get_copy_key(value)))
                del copy_dict[get_copy_key(value)]

        if len(values) > 1:
            if ( (int(price_dict.get(values[0])) - int(price_dict.get(ID_item)))  < (int(price_dict.get(values[1])) - int(price_dict.get(ID_item))) ):
                print("You may, also, consider: {}, {}, {}".format( values[0] , mi_dict[values[0]] , price_dict.get(values[0])  ))
            else:
                print("You may, also, consider: {}, {}, {}".format(values[1],mi_dict[values[1]],  price_dict.get(values[1]) ))
        else:
            print("You may, also, consider: {}, {}, {}".format(values[0],mi_dict[values[0]], price_dict.get(values[0]) ))
    else:
        print("No such item in inventory")
    user_input = input("Enter manufacturer and item type")