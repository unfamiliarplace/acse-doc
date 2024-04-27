ICS3U

# Programming Quiz 1 (b)

**Name: ______________________**

## (1) Concepts

*Answer in full sentences.*

(a) Why might you use `//` instead of just `/` sometimes? e.g. compare `(7 // 5)` and `(7 / 5)`.
<br><br><br><br><br><br><br>
(b) These operations all have the same output. Explain why.

```
3 % 3   == 0
4 % 4   == 0
15 % 3  == 0
16 % 4  == 0
303 % 3 == 0
404 % 4 == 0
```
<br><br><br><br><br><br>
(c) What is the highest index you can access in the string `'cat'`?
<br><br><br><br><br><br><br><br>

<div style="page-break-after: always"></div>

## (2) Predict output

*Write any output the terminal would show after running the block of code.<br>No explanations are necessary.*

(a)
```
x = 2 * 2
y = x * x
z = x
x = 0
if z == x:
  print('Yay)
else:
  print('Nay')
```
<br><br>

(b)
```
L = ['mom', 'dad', 'brother', 'sister']
L.sort()
print(L[:2])
```
<br><br>

(c)
```
n = 15
if n > 10:
  print('A')
elif n > 5:
  print('B')
if n > 0:
  print('C')
elif n < 20:
  print('D')
else:
  print('E')
```

<div style="page-break-after: always"></div>

## (3) Identify error

*Identify the part of the code that produces an error and explain why it does. For a bonus mark, name the specific error the way Python does.*

(a)
```
lifespan = 80
age = input('Enter your age: ')
print(lifespan - age)
```
<br><br><br>

(b)
```
password = 123RuBy$
attempt = input('Enter your password: ')
if attempt == password:
  print('Correct!')
else:
  print('Incorrect!')
```
<br><br><br>

(c)
```
ages = [7, 9, 10]
ages.remove(7)
print(ages[2])
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
# Output the last 2 characters of a string
s = 'this is just an example, pretend it could be any string'

print(___________________________)
```

<div style="page-break-after: always"></div>

## (5) Document code

*Read this code block.*

```
x = int(input())
y = int(input())
z = x / y * 100
if z >= 50:
  print('')
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
