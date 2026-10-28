#!/usr/bin/env python3

import math 
def main():
    user_input = input("Give me a number :")
    number = float(user_input)

    result = int(math.ceil(number))
    print(result)

if __name__ == "__main__":
    main()

