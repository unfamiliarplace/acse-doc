# 1. What does this code do?
# 2. Give each variable text logical name

text = input()
subtext = input()

if subtext in text:
    print(text.count(subtext))
else:
    print('0')

# Ask for two texts
# If the second occurs inside the first, print how many times it does
# Otherwise print '0'
