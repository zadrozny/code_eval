#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/18/
# Multiples of a number


import sys
from copy import copy

f = open(sys.argv[1], 'rU')                             # Load lines


for l in f:
    x, n = [int(n) for n in l.strip('\n').split(',')]
    v = copy(n)
    i = 1
    while v < x:
        v = i*n
        i+=1
    print(v) 
