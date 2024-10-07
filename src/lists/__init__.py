
section = """
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
messenger = ["\\nMessenger:", "This", "is", "madness..."]
leonidas = ["\\nLeonidas:", "Madness?", "This", "is", "Sparta!"]
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


"""