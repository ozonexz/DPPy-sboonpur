#!/usr/bin/env python3

import sys 

def downcase_it (s):
    return s.lower()

def main():
    if len(sys.argv) < 2:
        print("none")
        return
    for arg in sys.argv[1:]:
        print(downcase_it(arg))

main()
