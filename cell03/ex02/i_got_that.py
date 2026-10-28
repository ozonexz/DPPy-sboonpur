#!/usr/bin/env python3

def main():
    response = input("What you gotta say? :")
    while True: #if u input sth that program it will do loop
        if response == "STOP":
            break
        response = input("I got that! Anything else? :")

if __name__ == "__main__":
    main()