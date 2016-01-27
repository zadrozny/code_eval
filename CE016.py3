#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/16/
# Number of ones


import sys


f = open(sys.argv[1], 'rU')                             # Load lines

for l in f:
    print(sum(1 for s in bin(int(l.strip('\n'))) if s == '1'))
