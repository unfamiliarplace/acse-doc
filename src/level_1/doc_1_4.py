# 1. What does this code do?
# 2. Give each variable a logical name

x = [19, 13, 15, 18, 22, 21, 14, 16, 19]
y = []

for z in x:
    if z >= 18:
        y.append(z)

print(f'____ {len(y)} out of {len(x)}')
