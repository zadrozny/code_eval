#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/14/
# String permutations


import sys
from itertools import permutations as perm


f = open(sys.argv[1], 'rU')                             # Load lines


for l in f:
    print(', '.join([''.join(p) for p in list(perm(l.strip('\n')))]))
