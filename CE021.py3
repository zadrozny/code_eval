#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/20/
# Sum of digits


import sys


f = open(sys.argv[1], 'rU')                             # Load lines


for l in f:
    print(sum(int(d) for d in l.strip('\n')))