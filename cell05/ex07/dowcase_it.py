#!/usr/bin/env python3

#want user to type only 1 parameter  
# it will keep a file name is 1 amd next is 2
import sys 

if len(sys.argv) == 2: 
    print(sys.argv[1].lower())
else:
    print("none")

