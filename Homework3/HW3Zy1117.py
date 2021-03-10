# Lauren Holley
# 1861058
list_input = input()
individual_elements = list_input.split()
number_list = []
for individual_element in individual_elements:
    number_list.append(int(individual_element))

pos_num = []
for num in number_list:
    if num >= 0:
        pos_num.append(num)
pos_num.sort()
for i in pos_num:
    print(i, end=" ")
