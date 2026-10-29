#!/usr/bin/env python3


def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red" , family))

dupont_family = {
    "florian": "red",   #name is a key and color is a value from dict
    "marie" : "blond",
    "virginie" : "brunette",
    "david" : "red",
    "franck" : "red",
}

print(find_the_redheads(dupont_family))

