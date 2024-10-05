from strings.slice import sliceOperator
from strings.forLoop import forLoop

def exampleOFStrings():
    oneString = "hello"
    anotherString = "world!"
    greetting = oneString + " " + anotherString
    print("greetting variable: " + greetting)

    print("\nwhile loops: ")
    index = 0
    while index < len(greetting):
        letter = greetting[index]
        index = index + 1
        print(letter)
        
    print("""
For loops:
    result=''
    for letter in greetting:
        result+= letter.upper()
    """)
    print("\treturns: " + forLoop(greetting, lambda letter: letter.upper()))

    print("\nSlicing in Python.\n\tThe colon operator ':' is used slicing strings.")
    print("\tEg: greetting[0:5] returns '" + sliceOperator(greetting, 0, 5) + "'." )