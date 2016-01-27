#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/13/
# Remove characters


import sys


f = open(sys.argv[1], 'rU')                             # Load lines


for l in f:                                             
	text, chars = l.strip('\n').split(', ')
	for char in chars:
		text = text.replace(char, '')
	print(text)		