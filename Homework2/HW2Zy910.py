# Lauren Holley
# 1861058
import csv
frequency = {}
file = input()
with open(file, 'r') as csvfile:
    word_reader = csv.reader(csvfile, delimiter=',')

    for row in word_reader:
        for word in row:
            if word not in frequency.keys():
                frequency[word] = 1
            else:
                frequency[word] +=1

for word in frequency:
    print(word, frequency[word])