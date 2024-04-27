# 1. What does this code do?
# 2. Give each variable a logical name

names = []

choice = input('Enter a name or Q to quit: ')
while choice.upper() != 'Q':
    if choice.isalpha():
        names.append(choice.title())

    choice = input('Enter a name or Q to quit: ')

print(f'Valid names:')
for name in names:
    print(name)

# Asks the user to enter names. Change each valid name entered
# to title case and print them out one by one. A valid name
# consists only of alphabetic characters. Stop asking for names
# when the user enters 'Q'.
