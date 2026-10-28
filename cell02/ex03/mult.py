a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = a * b

print(f"{a} x {b} = {c}")

if c == 0:
    print("the result is positive and negative.")
elif c > 0:
    print("the result is positive.")
elif c < 0:
    print("the result is negative.")

