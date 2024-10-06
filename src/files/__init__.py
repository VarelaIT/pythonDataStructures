
section = """
## Files:

Open file and return a corresponding _file object_. If the file cannot be opened, an OSError is raised.

file is a path-like object giving the pathname (absolute or relative to the current working directory) 
of the file to be opened or an integer file descriptor of the file to be wrapped. 
(If a file descriptor is given, it is closed when the returned I/O object is closed unless closefd is set to False.).
"""
def workingWithFiles():
    print(section)
    try:
        file = open("README.md", "a")
        print(file)
    except:
        print("Error: can't read file.")
