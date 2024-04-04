#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need
to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    next_byte = 0
    for byte in data:
        if next_byte > 0:
            if byte >> 6 != 0b10:
                return False
            next_byte -= 1
        else:
            '''
            checking for:
                1. single-byte character
                2. two-byte character
                3. three-byte character
                4. four-byte character
            '''
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                next_byte = 1
            elif byte >> 4 == 0b1110:
                next_byte = 2
            elif byte >> 3 == 0b11110:
                next_byte = 3
            else:
                return False
        if next_byte < 0:
            return False
    return next_byte == 0
