# Python Data Structures

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
while index < len(gretting):
    letter = fruit[index]
    print(letter) 
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
