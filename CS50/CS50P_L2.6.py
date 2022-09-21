# Square pattern program with nested loops

# Program 1 - a program that prints out a 3 x 3 square
def main():
    print_square(3)

def print_square(size):
    for i in range(size): # For each row in square
        for j in range(size): # For each brick in row
            print("#", end="") # Print brick
        print() # Prints out a blank new line

main()

# Program 2 - another way to code Program 4
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size) 
        
main()

# Program 3 - another way to code Program 4
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()