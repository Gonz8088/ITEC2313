# Modify the program below
"""
File: encrypt.py
Probject 4.1

Encypts an input string of the ASCII characters and prints
the result.  The other input is the distance value.
"""

# The ASCII values range from 0 through 127

plainText = open(input("Enter the input file name: "))
distance = int(input("Enter the distance value: "))
code = ""
for line in plainText:
    for ch in line:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > 127:
            cipherValue = distance - (127 - ordValue + 1)
        code +=  chr(cipherValue)
print(code)
