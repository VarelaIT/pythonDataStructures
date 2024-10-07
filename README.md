
# Python Data Structures

Learning Python data structures. this document is generated by code itself I hope you enjoy it.

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

## Files

In Python you can obtain the instance of a `file` by using the `open` built-in function.

File is a path-like object giving the pathname (absolute or relative to the current working directory) 
of the file to be opened or an integer file descriptor of the file to be wrapped. 
(If a file descriptor is given, it is closed when the returned I/O object is closed unless closefd is set to False.).

### `open` function
Open file and return a corresponding _file object_. If the file cannot be opened, an OSError is raised.
 
**Open Syntax**
```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

Mode is an optional string that specifies the mode in which the file is opened. It defaults to 'r' which means open for reading in text mode.

|Char|Meaning|
|----|-------|
|'r'|open for reading (default)|
|'w'|open for writing, truncating the file first|
|'x'|open for exclusive creation, failing if the file already exists|
|'a'|open for writing, appending to the end of file if it exists|
|'b'|binary mode|
|'t'|text mode (default)|
|'+'|open for updating (reading and writing)|

Example of the code that writes this document:
```python
try:
    file = open("README.md", "w")
    file.write(content)
    print("File writed.")
except:
    print("Error: can't read or write file.")
```

### Reading files

`File.read()` Reads a whole file returning a string.

`File.readlines()` Reads the file returning an array of a string per line.
```python
fHanddler = open(fileName, "r")
lines = fHanddler.readlines()
for line in lines:
    print(line)
```

Here's the output of a function that reads the first 10 lines of this very file:
```md

# Python Data Structures

Learning Python data structures. this document is generated by code itself I hope you enjoy it.

## String

A string is a sequence of characters.
```python
oneString = "hello" #>>> hello

```


## Lists

List are collection of data.
```python
leonidas = ["This", "is", "Sparta!"]
len(stringList) # returns 3
```

The `range` function an integer representing a size 
and returns a list ordered numbers starting from 0.
```python
for i in range(len(stringList)):
    print(i, stringList[i])
```

The contateantion operator `+` concatenates lists returning a new list.
```python
result = ""
messenger = ["\nMessenger:", "This", "is", "madness..."]
leonidas = ["\nLeonidas:", "Madness?", "This", "is", "Sparta!"]
dialog = messenger + leonidas
for word in dialog:
    result += word + " "
print(result)
'''
Messenger: This is madness...
Leonidas: Madness? This is Sparta!
'''
```

### List Methods

#### `append`

Adds an element to de end of the list.
```python
ages = [18, 22, 30, 25]
ages.append(27) # now: [18, 22, 30, 25, 27]
```

#### `extend`

Extend the list by appending all the items from the iterable.
```python
ages = [18, 22, 30, 25]
ages.extend([27, 19, 37]) # now: [18, 22, 30, 25, 27, 19, 37]
```

#### `insert`

Insert an item at a given position. The first argument is the index of the element before which to insert.
```python
ages = [18, 22, 30, 25]
ages.insert(0, 27) # now: [27, 18, 22, 30, 25]
```



## Credits

**Ismael Varela**, Fulstack Developer
