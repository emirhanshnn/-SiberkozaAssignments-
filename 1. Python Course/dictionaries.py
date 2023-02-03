# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
person_es = {
    "name" : "Emirhan",
    "surname" : "Şahin",
    "age" : 21
}
print(person_es)

# Get value
print(person_es["age"])

# Add key/value
person_es["number"] = "123456"
print(person_es.keys())
print(person_es.values())
print(person_es.items())

# Remove item
del(person_es["age"])
person_es.pop("number")
print(person_es)

#Length
print(len(person_es))

#Clear
person_es.clear()
print(person_es)

#List of Dict

people = [
    {"name": "Emirhan", "surname": "Şahin"},
    {"name": "emir", "surname": "shn"}
]
print(people[0]["name"])