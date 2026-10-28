#!/usr/bin/env python3
# use usr to allow the terminal to run the program without having to type python3 before the file name
num = int(input("Enter a number less than 25: \n"))
if num > 25:
    print("Error")
else:
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1


