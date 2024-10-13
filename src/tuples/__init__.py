
from typing import List


section = """
## Tuples

Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). 
Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a `set` or `dict` instance).
```python
tuple('abc') # returns ('a', 'b', 'c') 
tuple( [1, 2, 3] ) # returns (1, 2, 3)
```

Tuples assignment:
```python
person = ("fred", 21)
name, age = person
print(name) # prints: fred
print(age) # prints: 21
```

The `>` & `<` operators
```python
(0, 23) > (-1, 24) # returns True
(0, 23) < (0, 24) # returns True
("Zod", "apple") > ("angel", "Ponking") # returns false
("Bob", "joe") < ("Bob", "tim") # returns false
```
### Example of a program that return the 10 most used words in this document.

```python
import files

def wordCount(lineList: List[str])-> dict:
    result = dict()
    for line in lineList:
        for word in line.split():
            result[word] = result.get(word, 0) + 1
    return result    

def sortDictByValue(dictionary: dict[str, int])-> List[tuple[int, str]]:
    result: List[tuple[int, str]] = []
    for word, count in dictionary:
        result.append(tuple(count, word))
    return sorted(result, reverse=True)


sortedList = tuples.sortDictByValue(tuples.wordCount(files.readFile(fileName)))
```
Here the result:
"""

def wordCount(lineList: List[str])-> dict:
    result = dict()
    for line in lineList:
        for word in line.split():
            result[word] = result.get(word, 0) + 1
    return result    

def sortDictByValue(dictionary: dict[str, int])-> List[tuple[int, str]]:
    result: List[tuple[int, str]] = []
    for word, count in dictionary.items():
        result.append((count, word))
    return sorted(result, reverse=True)    

def printWordsCount(topTenWords: List[tuple[int, str]])->str:
    result = """
|Word|Times|
|----|-----|
"""
    for count, word in topTenWords:
        result = result + "|" + word + "|" + str(count) + "|\n"
    return result