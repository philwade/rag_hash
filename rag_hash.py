#! /usr/bin/python
import sys

toHash = sys.argv[1]

count = 0
hashed = ''

for char in toHash:
    count += 1
    if count == 8:
        hashed += '8'
        count = 0
    else:
        hashed += char

print hashed
