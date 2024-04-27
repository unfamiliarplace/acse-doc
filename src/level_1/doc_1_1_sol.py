# 1. What does this code do?
# 2. Give each variable a logical name

# Asks the user for some text
# Counts the punctuation
# Outputs the number of punctuation characters

text = input('Enter text: ')

punctuation_tally = 0
for char in text:
    if char in '.,!?;:':
        punctuation_tally = punctuation_tally + 1

print(punctuation_tally)
