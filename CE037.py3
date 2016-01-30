#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/37/
# Pangrams

import string
import sys


f = open(sys.argv[1], 'rU')   


for l in f:
    dif = set(string.ascii_lowercase)-set(l.strip('\n').lower())
    if dif:
        print(''.join(sorted(list(dif))))
    else:
    	print('NULL')