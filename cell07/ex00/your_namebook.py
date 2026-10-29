#!/usr/bin/env python3

def array_of_name(persons):
    result = []
    for first, last in persons.items():
        full_name = first.capitalize() + " " + last.capitalize()
        result.append(full_name)

    return result 

persons = {
    "jean": "valijean", 
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier",
}

print(array_of_name(persons))
