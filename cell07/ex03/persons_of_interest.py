#!/usr/bin/env python3

def famous_births(people):
    sorted_people = sorted(people.values(), key=lambda p: p["date_of_birth"])
    for person in sorted_people:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}. ")

woman_scientists = {
    "ada" : {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Ceilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
}
famous_births(woman_scientists)
