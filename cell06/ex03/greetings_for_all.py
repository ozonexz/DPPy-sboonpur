#!/usr/bin/env python3

def greeting(name="noble stranger"): #noble is a defult parameters name = get a parameters
    if isinstance(name, str):
        print(f"Hello, {name}. ")
    else:
        print("Error! It was not a name.")

greeting("Alexandra")
greeting('Wil')
greeting()
greeting(42)
