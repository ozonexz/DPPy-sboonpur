#!/usr/bin/env python3

import sys

#name.py mean aray[0] it will only print [1] if dont have [1] will print none
if len(sys.argv) > 1: #we dont us = because program will understand we assignment 
    print(sys.argv[1])
else:
    print("none")

#more question on gemini