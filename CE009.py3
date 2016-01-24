#!/usr/bin/python3
# -*- coding: utf-8 -*-

# CodeEval problem 9: https://www.codeeval.com/open_challenges/2/

import sys


f = open(sys.argv[1], 'r')

for l in f:
	stack = [int(n) for n in l.strip('\n').split()]
	for e in range(1, len(stack) + 1):
		if e % 2 != 0:
			print(stack.pop(), end=' ')
		else:
			stack.pop()
	print(end='\n') 			
