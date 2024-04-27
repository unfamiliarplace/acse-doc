# 1. What does this code do?
# 2. Give each variable a logical name

x = int(input('Enter a number: '))

while x % 2 != 0:
    print('Try again')
    x = int(input('Enter a number: '))

print('That will do')
