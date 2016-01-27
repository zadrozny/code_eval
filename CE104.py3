#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/104/
# Word to digit


import sys


f = open(sys.argv[1], 'rU')                             # Load lines



table = ['zero', 'one', 'two', 'three', 'four', 
         'five', 'six', 'seven', 'eight', 'nine']

for l in f:
    words = l.strip('\n').split(';')
    digits = ''.join([str(table.index(w)) for w in words])
    print(digits)