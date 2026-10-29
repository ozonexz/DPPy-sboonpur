#!/usr/bin/env python3

import sys
import re #new module call re method is re.findall

def main():
    #check if we get a 2 parameters
    if len(sys.argv) != 3: # != mean not equal
        print("none")
        return
    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(re.escape(keyword) ,text)

    if not matches or keyword == "":
        print("none")
    else:
        print(len(matches))

main()

#check the string that appears 2 or 3 or 1 times
