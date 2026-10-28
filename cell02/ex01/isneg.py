#use if one by one to check if the number is negative, positive or zero.
#!/usr/bin/env python3


number = int(input().strip())

if number < 0:
    print("this number is negative.")
elif number > 0:
    print("this number is positive.")
else:
    print("this number is both negative and positive.")

