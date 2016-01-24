#!/usr/bin/python3
# -*- coding: utf-8 -*-

# CodeEval problem 10: https://www.codeeval.com/open_challenges/10/

import sys


f = open(sys.argv[1], 'r')

for l in f:
	*chars, i = l.strip('\n').split()
	if int(i) <= len(chars):
		print(chars[-int(i)])
