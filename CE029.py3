#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/29/
# Unique elements


import sys

f = open(sys.argv[1], 'rU')                           # Load lines


for l in f:
    print(','.join(sorted(set(l.strip('\n').split(',')))))
