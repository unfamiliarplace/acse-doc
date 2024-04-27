# 1. What does this code do?
# 2. Give each variable a logical name

ages = [19, 13, 15, 18, 22, 21, 14, 16, 19]
valid_ages = []

for age in ages:
    if age >= 18:
        valid_ages.append(age)

print(f'Found {len(valid_ages)} people old enough to vote out of {len(ages)} total')

# Goes through a list of numbers (ages?) and keeps only the ones
# greater or equal to 18.
