#! /usr/bin/python
import sys

toHash = sys.argv[1]

print ''.join([toHash[i] if (i + 1) % 8 != 0 else '8' for i in range(len(toHash))])
