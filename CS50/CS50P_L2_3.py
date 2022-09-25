# A program that utilizes loops while also validating user input

# Program 1 -asks for user input then prints "meow" n amount of times
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")

# Program 2 - better way to code Program 1
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
