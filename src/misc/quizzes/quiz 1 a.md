ICS3U

# Programming Quiz 1

**Name: ______________________**

## (1) Concepts

*Answer in full sentences.*

(a) Explain why you would use `int(input())` instead of just `input()` in some cases.
<br><br><br><br><br><br><br>
(b) Explain the modulo operator (`%`). Here are some examples to jog your memory.

```
2 % 2 == 0
3 % 2 == 1
7 % 4 == 3
8 % 3 == 2
8 % 6 == 2
```
<br><br><br><br><br><br>
(c) What are three of the many things that can be done with both a `str` and a `list`?<br>(Not counting `print`ing them or assigning a variable.)
<br><br><br><br><br><br><br><br>

<div style="page-break-after: always"></div>

## (2) Predict output

*Write any output the terminal would show after running the block of code.<br>No explanations are necessary.*

(a)
```
a = 17
x = a
y = x - 10
x = x - 7
z = y + x
if z == a:
  print('Yay')
else:
  print('Nay')
```
<br><br>

(b)
```
L = ['apple', 'orange', 'banana', 'kiwi']
L.sort()
print(L[1:4])
```
<br><br>

(c)
```
n = 25
if n > 30:
  print('A')
elif n > 20:
  print('B')
if n > 10:
  print('C')
elif n < 30:
  print('D')
else:
  print('E')
```

<div style="page-break-after: always"></div>

## (3) Identify error

*Identify the part of the code that produces an error and explain why it does. For a bonus mark, name the specific error the way Python does.*

(a)
```
long_word = 'kind'
short_word = long_word - 'd'
print(f'A little more than {short_word} and less than {long_word}')
```
<br><br><br>

(b)
```
import random
secret = random.randint(1, 100)
n = int(input('Enter a number from 1 to 100: '))
if n = secret:
  print('You guessed it!')
```
<br><br><br>

(c)
```
ages = [15, 14, 18, 17]
print(ages[4])
```
<br><br><br>

<div style="page-break-after: always"></div>

## (4) Write code

*Fill in the missing code based on the comments.*

(a)
```
# Ask a user to enter a sentence
# Print the number of characters in the sentence

sentence = __________________________

_____________________________________
```
<br>

(b)
```
# The user has tried to guess a secret number.
# Tell them whether it's too high or too low.

import random
secret = random.randint(1, 100)
guess = int(input('Enter a guess: '))

_____________________________________

_____________________________________

_____________________________________

_____________________________________
```
<br>

(c)
```
# Output the last 3 items in the list
L = ['just', 'an', 'example', 'list', 'contents', 'could', 'be', 'anything']

print(___________________________)
```

<div style="page-break-after: always"></div>

## (5) Document code

*Read this code block.*

```
x = input('')
y = int(input(''))
z = int(input(''))
if y <= z:
  print(x[y:z])
else:
  print('')
```

*(a) Explain what the code does in full sentences.*
<br>
<br>
<br>
<br>
<br>
<br>
<br>

*(b) Give the variables better names.*
<br><br>
`x`: ____________________
<br><br>
`y`: ____________________
<br><br>
`z`: ____________________
<br><br>

## (999) Bonus mark opportunities

*Tell me about some programming concept I didn't ask you about.*

<br><br><br><br>
<br>

*How are you finding programming so far? Anything fun about it? Anything hard about it?*
