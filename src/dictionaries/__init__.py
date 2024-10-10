
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
# now count = {"Ismael": 3, "Ruben": 1, "Sohany": 2}
```

### Methods

### `get`
```python
cesarCount = count.get("Cesar", 0) # There no key Cesar in count so cesarCount = 0
ismaelCount = count.get("Ismael", 0) # ismaelCount = 3
```

"""