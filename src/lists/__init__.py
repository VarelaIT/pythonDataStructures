
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

### Operators

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

The `in` operator returns a boolean if a value belongs to a `list`.
```python
leonidas = ["This", "is", "Sparta!"]
if("Sparta!" in leonidas):
    return True
```

### List Methods

### `append`

Adds an element to de end of the list.
```python
ages = [18, 22, 30, 25]
ages.append(27) # now: [18, 22, 30, 25, 27]
```

### `extend`

Extend the list by appending all the items from the iterable.
```python
ages = [18, 22, 30, 25]
ages.extend([27, 19, 37]) # now: [18, 22, 30, 25, 27, 19, 37]
```

### `insert`

Insert an item at a given position. The first argument is the index of the element before which to insert.
```python
ages = [18, 22, 30, 25]
ages.insert(0, 27) # now: [27, 18, 22, 30, 25]
```

### `remove`

Removes the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
```python
ages = [18, 22, 30, 25]
ages.remove(25) # now: [18, 22, 30]
```

### `pop`

Removes the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
```python
ages = [18, 22, 30, 25]
ages.pop() # now: [18, 22, 30]
ages.pop(0) # now: [22, 30]
```

### `clear`

Remove all items from the list. 
```python
ages = [18, 22, 30, 25]
ages.clear() # now: []
```

### `index`

Return zero-based index in the list of the first item whose is equal to the argument passed in the first position.
Can take 2 optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
Raises a ValueError if there is no such item.

```python
ages = [18, 22, 30, 25]
ages.index(30) # returns: 2
```

### `count`

Return the number of times given value appears in the list.
```python
ages = [18, 22, 30, 25]
ages.count(18) # returns: 1
```

### `sort`

Sort the items of the list in place.
```python
ages = [18, 22, 30, 25]
ages.sort() # now: [18, 22, 25, 30]
```


### `reverse`

Reverse the elements of the list in place.
```python
ages = [18, 22, 30, 25]
ages.reverse() # now: [25, 30, 22, 18]
```

### `copy`

Return a shallow copy of the list.
```python
ages = [18, 22, 30, 25]
ages.copy() # returns: [18, 22, 30, 25]
```

"""