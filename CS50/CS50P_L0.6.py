# simple calculator with def and return functions

def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return n * n # can also be writen n ** 2 or pow(n, 2)

main()