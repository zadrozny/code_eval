#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://www.codeeval.com/open_challenges/26/
# Print file size


import os
import sys

f = sys.argv[1]                           # Load lines


print(os.path.getsize(f))
