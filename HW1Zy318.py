# Lauren Holley
# 1861058
import math
w_height = int(input("Enter wall height (feet):"))
print()
w_width = int(input("Enter wall width (feet):"))
print()
area = w_height * w_width
print("Wall area:", area, "square feet")
paint_sqft = 350
print("Paint needed:", ('{:.2f}'.format(area / paint_sqft)), "gallons")
cans_needed = math.ceil(area / paint_sqft)
print("Cans needed:", cans_needed, "can(s)")
print()
choose_color = input("Choose a color to paint the wall:")
print()
cost = {
    'red': 35,
    'blue': 25,
    'green': 23
}
total_cost = cost[choose_color] * cans_needed
print("Cost of purchasing", choose_color, "paint: $", end='')
print(total_cost)
