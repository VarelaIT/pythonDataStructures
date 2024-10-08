
section = """
## String

A string is a sequence of characters.
```python
oneString = "hello" #>>> hello
anotherString = "world!" #>>> world!
```

The contatenate operator it the `+` symbol.
```python
gretting = oneString + " " + anotherString #>>> hello world!
```

The `len` function take a string argument and returns interger representing the length of a string.
```python
len(gretting) #>>> 12
```

Looping through strings
```python
index = 0
while index < len(greetting):
    letter = fruit[index]
    index = index + 1
    print(letter) 

for letter in greetting:
    print(letter)

#both loops will print: 
#>> h
#>> e
#>> l
#>> l
#>> o
#>> 
#>> w
#>> o
#>> r
#>> l
#>> d
#>> !
```

### String methods

### `split`

The `split` method divide the `string` by the white spaces, returning a `list` with the resulting strings.
It takes an optional `string` argument in order to change the delimiter.
```python
sentence = "With three words."
words = sentence.split() # returns ["With", "three", "words."]
```
"""

def stringSection() -> str:
    return ""