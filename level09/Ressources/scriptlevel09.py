#! /usr/bin/python3
import sys
result = ""
for i, c in enumerate(sys.argv[1]):
    result += chr(ord(c) + i)
