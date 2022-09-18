# program implementing the modulo operation


# Program 1 - determining whether a number is an even or odd number
x = int(input("What's x?"))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Program 2 - defining a main function
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else: 
        return False

main()

# Program 3 - example 1 with Pythonic expressions 
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()

# Program 4 - example 2 with Pythonic expressions
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()