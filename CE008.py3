#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/8/
# Reverse Words


import sys


f = open(sys.argv[1], 'r')

for l in f:
    if l == '\n':
        continue
    print(' '.join(l.split()[::-1]))