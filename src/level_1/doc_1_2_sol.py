# 1. What does this code do?
# 2. Give each variable a logical name

n = int(input('Enter a number: '))

while n % 2 != 0:
    print('Try again')
    n = int(input('Enter a number: '))

print('That will do')

# Ask the user to input a number until they enter an even one
