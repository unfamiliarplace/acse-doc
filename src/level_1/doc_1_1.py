# 1. What does this code do?
# 2. Give each variable a logical name

x = input('Enter x: ')

y = ''
for z in x:
    if z in 'aeiouAEIOU':
        y = y + z

print(y)
