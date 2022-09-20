# program using the dictionary data structure
# dicts or dictionaries are a data structure that allows you to associate a key with a value
# dictionaries are like an associative array that consists of a collection of key-value pairs

# Program 1 - a program with a single dictionary
students = { # the curly braces represents that this is a dictionary
    "Hermione": "Gryffindor", # Hermione is the key, Gryffindor is the value
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

# Program 2 - a program with a list of dictionaries
students = [ # the square brackets represents that this is a list
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, # this line represents a dictionary in the list
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, # second dictionary 
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"}, # third dictionary
    {"name": "Draco", "house": "Slytherin", "patronus": None} # fourth dictionary
]
# notice how the dictionaries all have the same keys (name, house, and patronus) but all of them have unique values

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")