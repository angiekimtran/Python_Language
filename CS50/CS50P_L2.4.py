# program utilizing a list, for loop, and len() function

# Program 1 - program that prints all the students in a list
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

# # Program 2 - better way to code Program 1 using for loop
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)


# len function tells us the length of a list
# Program 3 - better way to code Program 2 using len function
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)): # nested functions
    print(i + 1, students[i])
