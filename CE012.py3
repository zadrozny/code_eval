#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/12/
# First non-repeated character


import sys


f = open(sys.argv[1], 'rU')                             # Load lines


for l in f:                                             
    for i in range(len(l)):                             # Iteratate over chars
    	lim = 0 if i == 0 else i                        # Avoid negative indices
    	if l[i] not in l[i+1:] and l[i] not in l[:lim]: # Look ahead and behind
    		print(l[i])
    		break
    else:
    	print('No non-repeated characters in', l)
    