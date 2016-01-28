#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/23/
# Multiplication table

for r in range(1, 13):
    print(''.join(['%4s' % (r*n) for n in range(1, 13)])[2:])
