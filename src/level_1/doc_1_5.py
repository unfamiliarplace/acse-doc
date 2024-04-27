# 1. What does this code do?
# 2. Give each variable a logical name

x = []

y = input('Enter a name or Q to quit: ')
while y.upper() != 'Q':
    if y.isalpha():
        x.append(y.title())

    y = input('Enter a name or Q to quit: ')

print(f'Valid names:')
for z in x:
    print(z)
