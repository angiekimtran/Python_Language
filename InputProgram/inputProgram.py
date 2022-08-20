#Ask user input for their first name and last name.
print('Answer these questions!')
first_name = input('What is your first name?')
last_name = input('What is your last name?')
print(first_name, last_name)
print(type(first_name))
print(type(last_name))

#Ask user to type in their age.
age = int(input('What is your age?'))
print(age)
print(type(age))

#Ask user to type in their GPA.
GPA = float(input('What was your GPA in school?: '))
print(GPA)
print(type(GPA))

#Ask user for their first and middle name.
first_name, middle_name = input ('Enter your first and middle name. Separate by a comma:').split(',')
print(first_name, middle_name)
