
section = """
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
|'w'| open for writing, truncating the file first|
|'x'| open for exclusive creation, failing if the file already exists|
|'a'| open for writing, appending to the end of file if it exists|
|'b'| binary mode|
|'t'| text mode (default)|
|'+'| open for updating (reading and writing)|

Example of the code that writes this document:
```python
try:
    file = open("README.md", "w")
    file.write(content)
    print("File writed.")
except:
    print("Error: can't read or write file.")
```
"""

def writeToFile(content: str):
    try:
        file = open("README.md", "w")
        file.write(content)
        print("File writed.")
    except:
        print("Error: can't read or write file.")
