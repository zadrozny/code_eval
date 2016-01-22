#!/usr/bin/python
# -*- coding: utf-8 -*-

# CodeEval problem 1: https://www.codeeval.com/open_challenges/1/

import sys

def fizzbuzz(inpt):
    X, Y, N = (int(n) for n in inpt.split())
    output = []
    for n in range(1, N+1):
        if n % X == 0 and n % Y == 0:
        	output.append('FB')
        elif n % X == 0:
        	output.append('F')
        elif n % Y == 0:
        	output.append('B')
        else:
        	output.append(str(n))
    return ' '.join(output)

# Sample code to read in test cases:

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(fizzbuzz(test))

test_cases.close()