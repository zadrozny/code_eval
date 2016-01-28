#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/23/
# Fibonacci 


import sys


f = open(sys.argv[1], 'rU')                             # Load lines


def fib(n):
    if n == 0: return 0

    if n == 1 or n == 2: return 1
    
    preceding, current = 1, 1
    i = 2
    while i < n:
        preceding, current = current, preceding + current
        i+=1

    return current


for l in f:
    print(fib(int(l.strip('\n'))))