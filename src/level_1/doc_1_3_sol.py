# 1. What does this code do?
# 2. Give each variable a logical name

illegal_chars = '<>:"/\|?*'
replacement_char = '_'
text = input('Enter some text: ')

for a in illegal_chars:
    text = text.replace(a, replacement_char)

print(f'Result: {text}')

# Ask for text. Replace each illegal (punctuation) character
# in the text with an underscore.
