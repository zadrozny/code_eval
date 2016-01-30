#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/46/
# Prime numbers

import sys


f = open(sys.argv[1], 'rU')   


def generate_primes_less_than(n):
    '''Return a list of primes less than n.'''

    if n <= 2: return []

    if n == 3: return [2]
    
    if n <= 5: return [2, 3]

    prime_list = [2, 3] # Intialize with 2 to skip evens

    for candidate in range(5, n, 2):       # Skip evens
        for prime in prime_list:            
            if candidate % prime == 0:      # It's not prime
                break   
            if prime > candidate / prime:   # It is prime
                prime_list.append(candidate)    
                break   
            
    return prime_list

for l in f:
    o = ','.join(map(str, generate_primes_less_than(int(l.strip('\n')))))
    print(o)