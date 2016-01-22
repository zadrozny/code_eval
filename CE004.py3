#!/usr/bin/python
# -*- coding: utf-8 -*-

def list_first_n_primes(n):
    '''Return a list of n primes'''

    if n == 0:
        return []

    if n == 1:
        return [2]

    if n == 2:
        return [2, 3]

    prime_list = [2, 3]  # Intialize with 2 to skip evens.

    candidate = 5	
    while len(prime_list) < n:
        for prime in prime_list:			
            if candidate % prime == 0:	# It's not prime.
                break	
            if prime > candidate / prime: # It is prime.
                prime_list.append(candidate) 	
                break
        candidate += 2	# Skip evens.			
				
    return prime_list

print(sum(list_first_n_primes(1000)))