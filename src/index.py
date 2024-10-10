import dictionaries
import lists
import strings
import files
import strings.stringDoc

fileName = "README.md"
title = """
# Python Data Structures

Learning Python data structures. this document is generated by code itself I hope you enjoy it.
"""
stringsSection = strings.stringDoc.section 
filesSection = files.getSectionContent(fileName, files.preContent, files.subContent)
footer = """
## Credits

**Ismael Varela**, Fulstack Developer
"""
content = title 
content += stringsSection
content += filesSection
content += lists.section
content += dictionaries.section
content += footer

files.writeToFile(fileName, content)

print("\nDone By Ismael Varela.\n")