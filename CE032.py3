#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/32/
# Trailing string


import sys

f = open(sys.argv[1], 'rU')                           # Load lines



for l in f:
    if l == '\n':
        print()
        continue
    s, sub = l.strip('\n').split(',')
    if sub in s[1:]:
        print(1)
    else:
        print(0)