# Lauren Holley
# 1861058
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
prices = {'-': 0, 'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
first_service = input("Select first service:")
print()
second_service = input("Select second service:")
print()
total_cost = prices[first_service] + prices[second_service]
print()
print("Davy's auto shop invoice")
print()
if first_service == '-':
    print("Service 1: No service")
else:
    print("Service 1: {}, ${}".format(first_service, prices[first_service]))

if second_service == '-':
    print('Service 2: No service')
else:
    print("Service 2: {}, ${}".format(second_service, prices[second_service]))
print()
print("Total: $", end='')
print(total_cost)