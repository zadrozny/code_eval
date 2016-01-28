#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/20/
# Lowercase


import sys


f = open(sys.argv[1], 'rU')                             # Load lines


for l in f:
    print(l.lower())