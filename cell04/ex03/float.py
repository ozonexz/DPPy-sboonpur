#!/usr/bin/env python3

user_input = input("Give me a number: " )

if float(user_input).is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
