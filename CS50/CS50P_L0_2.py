# Practice program from Harvard's CS50P lecture 0 on Python function and variables

# Example 3 - prints fist name
# Ask user for their name, remove whitespace from str, and capitalize user's name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}!")


# Example 4 - prints last name
# Ask user for their name, remove whitespace from str, and capitalize user's name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {last}!")
