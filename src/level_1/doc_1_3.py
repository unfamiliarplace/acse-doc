# 1. What does this code do?
# 2. Give each variable a logical name

x = '<>:"/\|?*'
y = '_'
z = input('Enter some text: ')

for a in x:
    z = z.replace(a, y)

print(f'Result: {z}')
