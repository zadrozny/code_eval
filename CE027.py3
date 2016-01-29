#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/27/
# Decimal to binary


import sys

f = open(sys.argv[1], 'rU')                           # Load lines


for l in f:
    if l == '\n':
        pass
    else:
        print(str(bin(int(l.strip('\n'))))[2:])
