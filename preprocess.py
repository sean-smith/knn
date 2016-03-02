#!/usr/bin/python

import sys
import fileinput

f1 = sys.argv[1]
f2 = sys.argv[2]

# replace '?' with 'b' in all lines
for f in (f1,f2):
	for line in fileinput.input(f, inplace=1):
	    sys.stdout.write(line.replace('?', 'b'))

# Check to make sure it worked.
for line in open(f1, "r+"):
	if line[0] == '?':
		print '?'

