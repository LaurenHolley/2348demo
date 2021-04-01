# Lauren Holley
# 1861058
# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) -1):
        index_largest = i
        for j in range(i +1, len(numbers)):
            if numbers[j] > numbers[index_largest]:
                index_largest = j
        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp
        print(" ".join(map(str, numbers))+" ")


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)