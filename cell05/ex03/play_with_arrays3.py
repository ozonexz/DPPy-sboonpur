#!/usr/bin/env python3

original_array = [ 2, 8, 9, 48, 8, 22,]

new_array = []
for num in original_array:
    if num > 5:
        new_array.append(num + 2)

new_set = set(new_array)

print(original_array)
print(new_set)
