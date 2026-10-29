#!/usr/bin/env python3

import sys


if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if not arg.endswith("ism"): 
            print(arg + "ism")

#use endswith to check if a arg end with ism or not? 
#it will skip a word that end with ism