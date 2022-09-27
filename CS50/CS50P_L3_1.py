# Practice program with exceptional cases using try statement, except statement, else clause, and while loop

# SyntaxError means that there's something wrong with the code written
# SyntaxError must be corrected by the programmer themselves
# Example of SyntaxError is print("Hello World)

# ValueError means that there is an invalid value in the code or from the user input
# Example of ValueError is print(int("cat"))

# NameError means that you're trying to use a variable or function that doesn't exist in the order of operation yet or wasn't used in a valid way
# Example of NameError is often when a variable or function is being used but has yet to be defined

# Program that repeats the prompt when user inputs an invalid value (something that is not an integer)
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError: # this tells Python what to do in exceptional cases
            pass    

main()
