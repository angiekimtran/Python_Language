# program that utilizes def function, while and for loop, and validates user input
# the program below asks for user input then prints "meow" n amount of times
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

# For the program above, we can still use break to break out of the loop but after the loop we must still return n
# This is demonstrated in the commented code below
# Notice how the return keyword below is outside of the loop but is still inside the function
# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#              break
#     return n
# Although we can use a break here, return is stronger than a break
# Return not only breaks out of a loop but also returns a value for you