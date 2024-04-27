ICS3U

# Function Pair Task

**Names: _________________________ and _________________________**

## Label parts of the function

### Word bank
```
function name
argument(s)
argument type(s)
return type
docstring description
docstring test cases
function body
return statement
```

### Label parts of this function
```
def cubic_root(x: int) -> float:
  """
  Return the cubic root of n. The cubic root is the number that equals
  n when cubed (raised to the power of 3). Accurate to within 1 decimal.

  >>> cubic_root(8)
  2.0
  >>> cubic_root(-8)
  -2.0
  >>> cubic_root(67)
  4.1
  """

  mult = 10 ** 3
  target = abs(x) * mult

  for n in range((target // 2) + 1):
      if (target - n ** 3) <= (1 / mult):
          break
  
  root = n / 10
  if x < 0:
      root *= -1

  return root
```

<div style="page-break-after: always"></div>

## Create documentation

Choose a good function name, give the argument type(s) and return type,
and write a docstring with a description and 3 examples showing different behaviour.

(a)

```
def _________________________(L: _________________) -> ____________:
  """

  _________________________________________________________________________

  _________________________________________________________________________


  >>> _________________________(_________________________)
  ______________
  >>> _________________________(_________________________)
  ______________
  >>> _________________________(_________________________)
  ______________
  """

  tally = 0
  for item in L:
    if is_prime_number(item):
      tally += 1
  return tally
```


(b)
Hint: This function takes two arguments, not one.

```
def _______________________(____: __________, ____: __________) -> __________:
  """

  _________________________________________________________________________

  _________________________________________________________________________


  >>> _________________________(_________________________)
  ______________
  >>> _________________________(_________________________)
  ______________
  >>> _________________________(_________________________)
  ______________
  """

  c_squared = a ** 2 + b ** 2
  return math.sqrt(c_squared)
```

<div style="page-break-after: always"></div>

## Implement documentation

For these ones, I've written the documentation, and your job is to write code to do what the documentation says. The code isn't meant to be challenging; this is more about reading the documentation correctly.

(a)

```
def can_castle(king_has_moved: bool, rook_has_moved: bool, path_is_clear: bool) -> bool:
  """
  Return True if the king and rook can castle.

  Castling is possible if neither the king nor the rook has moved
  and the path between them is clear. Otherwise, it's impossible.

  >>> can_castle(False, False, True)
  True
  >>> can_castle(True, False, True)
  False
  >>> can_castle(False, False, False)
  False
  """










```
<div style="page-break-after: always"></div>


(b)

```
def try_to_buy_item(price: int, paid: int) -> list[bool, int]:
  """
  Tries to buy an item and returns the result and amount of change.
  
  Specifically, if the amount paid is enough, return True and the amount
  of change to give. Otherwise, return False and 0 for the change.

  >>> try_to_buy(500, 700)
  [True, 200]
  >>> try_to_buy(1000, 100)
  [False, 0]
  >>> try_to_buy(0, 0)
  [True, 0]
  """









  
```
