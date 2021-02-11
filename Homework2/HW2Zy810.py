# Lauren Holley
# 1861058
phrase = input()
new_phrase = phrase.replace(" ", "")

if new_phrase == new_phrase[::-1]:
    print('{} is a palindrome'.format(phrase))
else:
    print('{} is not a palindrome'.format(phrase))
