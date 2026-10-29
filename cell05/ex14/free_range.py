#!/usr/bin/env python3

import sys  #[0] is a name of a file 
if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1]) #[1] mean a first parameters
    end = int(sys.argv[2]) #[2] mean a second parameters
    print(list(range(start, end + 1 ))) 
#use end +1 because it will end with a number -1 its how python count a num 

