# Practice program with nested loops

# Program 1 - a program that prints out and stacks three hashes
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

# Program 2 - another way to code Program 1
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()

# Program 3 - a program that prints out a row of question marks
def main():
    print_row(4)

def print_row(width):
    print("?" * width, end="\n")

main()

# Program 4 - a program that prints out a 3 x 3 square
def main():
    print_square(3)

def print_square(size):
    for i in range(size): # For each row in square
        for j in range(size): # For each brick in row
            print("#", end="") # Print brick
        print() # Prints out a blank new line

main()

# Program 5 - another way to code Program 4
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size) 
        
main()

# Program 6 - another way to code Program 4
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()