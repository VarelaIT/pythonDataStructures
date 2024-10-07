
from typing import List


preContent = """
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
"""
subContent = """
```

"""

def getSectionContent(fileName: str, preContent: str, subContent: str)-> str:
    result = preContent
    lines = readFile(fileName)
    index = 0
    linesCount = len(lines)
    limit = 10
    if(linesCount < limit):
        limit = linesCount
    while(index < limit):
        result += lines[index]
        index += 1
    return result + subContent
        
def readFile(fileName: str)-> List[str]:
    try:
        fHanddler = open(fileName, "r")
        lines = fHanddler.readlines()
    except:
        print("Error: File " + fileName + " could not be read.")
    return lines

def writeToFile(fileName: str, content: str):
    try:
        file = open(fileName, "w")
        file.write(content)
        print("File writed.")
    except:
        print("Error: can't read or write file.")
