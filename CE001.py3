#!/usr/bin/python
# -*- coding: utf-8 -*-

# CodeEval problem 1: https://www.codeeval.com/open_challenges/1/

def fizzbuzz(l):
    X, Y, N = (int(n) for n in l.strip('\n').split())
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


# Inputs: 3 5 10 and 2 7 15
tests = ['1 2 F 4 B F 7 8 F B', '1 F 3 F 5 F B F 9 F 11 F 13 FB 15']


with open('CE001.txt', 'r') as f:
    for i, l in enumerate(f):
	    assert fizzbuzz(l) == tests[i], 'test {} failed'.format(i)
