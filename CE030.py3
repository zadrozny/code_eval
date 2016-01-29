#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/30/
# Set intersection


import sys

f = open(sys.argv[1], 'rU')                           # Load lines


for l in f:
    one, two = l.strip('\n').split(';')
    one, two = one.split(','), two.split(',')
    print(','.join([n for n in sorted(one) if n in two]))
