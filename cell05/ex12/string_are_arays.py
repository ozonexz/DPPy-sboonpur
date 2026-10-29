#!/usr/bin/env python3

import sys 
if len(sys.argv) != 2: #len = count a member in the list or argument
    print("none")
else:
    count = sys.argv[1].count("z")
    print("z" * count if count > 0 else "none")

#check is there a z in the parameter or not if it not print none or 
# if dont have any parameter none too
