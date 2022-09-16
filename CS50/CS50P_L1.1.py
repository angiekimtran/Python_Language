# this program compares values using the conditional if, elif, and else

# relational operators:
# > greater than
# >= greater than or equal to
# < less than
# < less than or equal to
# == equality
# != not equal to

# Program 1 with if statements
x = int(input("What's x? "))
y = int(input("What's y? "))

# x < y is an example of a boolean expression
# a boolean expression - a question that has a yes or no / true or false answer
# indentation - tells Python that line 18 should only be executed if the answer to line 17 is true
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y: 
    print("x is qual to y")



# Program 2 with if and elif statements
# This program is more efficient than the first program
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y: 
    print("x is qual to y")

# Program 3 with if, elif, and else statements
# This program is more efficient and simple than the first and second program
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: 
    print("x is qual to y")
