#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/24/
# Sum of integers form a file

import sys

f = open(sys.argv[1], 'rU')                             # Load lines

print(sum([int(l.strip('\n')) for l in f]))
