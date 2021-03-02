# Lauren Holley
# 1861058
from datetime import date as dt
import datetime

file_name = input()
f = open(file_name, 'r')
date_line = f.read()
date_format = "%B %d, %Y"
individual_date = date_line.split("\n")
correct_date = []
for date in list(individual_date):
    try:
        datetime.datetime.strptime(date, date_format)
        correct_date.append(date)
    except ValueError:
        continue

month_dict = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5,
'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10,
'November' : 11, 'December' : 12 }

list_date = []
for date in correct_date:
    month_index = date.find(' ')
    month_name = date[0:month_index]
    num_month = month_dict[month_name]
    day = date[month_index+1:-6]
    year = date[-4:]
    new_date_string = ('{}/{}/{}'.format(num_month,day,year))
    list_date.append(new_date_string)

today = datetime.datetime.today()
current_date = today.strftime('%m/%d/%Y')

for date in list_date:
    if datetime.datetime.strptime(current_date,'%m/%d/%Y') > datetime.datetime.strptime(date,'%m/%d/%Y'):
        print(date)
    else:
        continue
