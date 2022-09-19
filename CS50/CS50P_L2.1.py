# practice prograam with the for loop

# Program 1 - program printing "meow" out three times
for i in [0, 1, 2]:
    print("meow")
    
# Program 2 - a better way to code Program 1
for i in range(3):
    print("meow")

# Program 3 - improvement from Program 2
# use an underscore to indicate that you don't care about the name of the variable
for _ in range(3):
    print("meow")

# Program 4 - another way to code Program 1
print("meow\n" * 3, end="")