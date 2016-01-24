#!/usr/bin/python
# -*- coding: utf-8 -*-

# CodeEval problem 2: https://www.codeeval.com/open_challenges/2/

import sys


f = open(sys.argv[1], 'r')

lines = reversed(sorted([l.strip('\n') for l in f.readlines()], key=len))

print('\n'.join(lines))

f.close()    