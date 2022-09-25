# def function 

# Practice 1 - poor formatting
def hello():
    print("Hello")

name = input("What's your name? ")
hello()
print(name)

# Practice 2 - better formatting
def hello(to):
    print("Hello", to)

name = input("What's your name? ")
hello(name)

# Practice 3 - hello() with no arugment
def hello(to="world"):
    print("Hello", to)

hello()
