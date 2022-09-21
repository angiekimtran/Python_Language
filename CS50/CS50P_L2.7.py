# Practice program printing patterns

# Program 1 - a program that prints out a stack of three hashes
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

# Program 3 - a program that prints out a row of 4 question marks
def main():
    print_row(4)

def print_row(width):
    print("?" * width, end="\n")

main()
