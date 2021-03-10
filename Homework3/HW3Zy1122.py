# Lauren Holley
# 1861058
list_input = input()
single_words = list_input.split(" ")
for word in single_words:
    w_count = single_words.count(word)
    print(word, w_count)
