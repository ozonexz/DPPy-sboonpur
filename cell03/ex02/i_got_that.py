#!/usr/bin/env python3

def main():
    response = input("What you gotta say? :")
    while True:
        if response == "STOP":
            break
        response = input("I got that! Anything else? :")

if __name__ == "__main__":
    main()
