# Lauren Holley
# 1861058
password = input()
end_char = 'q*s'
new_char = ''
for char in password:
    if char == 'i':
        password = password.replace('i','!')
    elif char == 'a':
        password = password.replace('a','@')
    elif char == 'm':
        password = password.replace('m', 'M')
    elif char == 'B':
        password = password.replace('B','8')
    elif char == 'o':
        password = password.replace('o','.')
    else:
        new_char += char

print(password+'q*s')