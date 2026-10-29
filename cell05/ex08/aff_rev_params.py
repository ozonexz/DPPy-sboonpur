#!/usr/bin/env python3

import sys 

def main():
    params = sys.argv[1:]

    if len(params) < 2:  #param < 2 it will show only none u have to text more than 1 string
        print("none")
    else:
        for param in reversed(params): #reversed use to switch a text from back to front 
            print(param)

main()
