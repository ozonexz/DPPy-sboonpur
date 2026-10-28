#!/usr/bin/env python3

def main():
    try:
        user_input = input("Enter a number ")
        number = int(user_input)
        for i in range (10):
            result = number * i
            print(f"{i} x {number} = {result}" )
    except ValueError:
        pass

if __name__ == "__main__":
    main()
#python will keep a module or file from being run when it is imported into another file. 
# The code in the if statement will only run if the file is being run directly, not if it is being imported.