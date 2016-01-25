#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/12/
# First non-repeated character


import sys


f = open(sys.argv[1], 'rU')



for l in f:
    for i in range(len(l)):
    	lim = 0 if i == 0 else i
    	if l[i] not in l[i+1:] and l[i] not in l[:lim]:
    		print(l[i])
    		break
    else:
    	print('No such character')
    