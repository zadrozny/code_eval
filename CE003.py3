#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/3/
# Write a program which determines the largest prime palindrome less than 1000. 
# Print to stdout the largest prime palindrome less than 1000. 

def is_prime(candidate):
    '''Return True if prime and False if not.'''

    if candidate <= 0:
        raise ValueError("Integer must be > 0; you entered: ", candidate)

    if candidate == 1: 
        return False 
		
    if candidate == 2:
        return True
	
    if candidate == 3:
        return True

    if candidate % 2 == 0:
        return False

    divisor = 3
    while divisor <= candidate / divisor:
        if candidate % divisor == 0:
            return False
        divisor += 2

    return True 


for n in range(1000, 2, -1):
    if n == int(str(n)[::-1]):
        if is_prime(n):
            print(n)
            break
