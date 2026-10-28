#!/usr/bin/env python3
import sys 

def advanced_mult():
    if len(sys.argv) > 1:
        print("none")
        return
    i = 0
    while i <= 10:
        print(f"Table de {i}: ", end="")
        j = 0
        while j <= 10:
            print(f" {i * j} ", end="")
            j += 1
        print()
        i += 1 

if __name__ == "__main__":
    advanced_mult()

