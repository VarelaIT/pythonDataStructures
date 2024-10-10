
section = """
## Dictionaries

Dictonaries are colection of data strored in key-value paris.

### Operators

The `in` operator:
```python
count = dict()
names = ["Ismael", "Ruben", "Sohany", "Sohany", "Ismael", "Ismael"]
for name in names:
    if name not in count:
        conunt[name] = 1
    else:
        count[name] += 1

for key, value in count: # supports 2 iteration variables.
    print(key, value)
# Prints the following: 
# Ismael 3
# Ruben 1 
# Sohany 2
```

### Functions

The `list` function takes a dictionary instance and returns a list of it.
```python
keyArray = list(count.keys()) # ["Ismael", "Ruben", "Sohany"]
valueArray = list(count.values()) # [3, 1, 2]
itemArray = list(count.items()) # [("Ismael", 3), ("Ruben", 1), ("Sohany", 2)]
```   

### Methods

### `get`
```python
cesarCount = count.get("Cesar", 0) # There no key Cesar in count so cesarCount = 0
ismaelCount = count.get("Ismael", 0) # ismaelCount = 3
```

"""