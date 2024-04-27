# 1. What does this code do?
# 2. Give each variable a logical name

# It asks the user for some text
# It only keeps the vowels from the text

text = input('Enter text: ')

only_vowels = ''
for char in text:
    if char in 'aeiouAEIOU':
        only_vowels = only_vowels + char

print(only_vowels)
