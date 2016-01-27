#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/18/
# Multiples of a number


import sys


f = open(sys.argv[1], 'rU')                             # Load lines


for l in f:
    x, n = [int(n) for n in l.strip('\n').split(',')]
    i = 1
    while n < x:
    	n*=i
    	i+=1
    print(n) 
