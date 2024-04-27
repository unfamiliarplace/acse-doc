# 1. What does this code do?
# 2. Give each variable a logical name

x = input('Enter x: ')

y = 0
for z in x:
    if z in '.,!?;:':
        y = y + 1

print(y)
