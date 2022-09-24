# Practice programs with command-line arguments and sys.argv 

import sys

# Program 1 - using a comand-line argument to print a name tag
# Type into the command line terminal the following: python {enter file name} {enter first name}
# The first element/location [0] in the list of sys.argv is the name of the file[0]
# The second element/location [1] in the list of sys.argv would be the name input[1] by the programmer
if len(sys.argv) < 2: # Checking for errors
    print("Too few arguments")
elif len(sys.argv) > 2: # Checking for errors
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1]) # Print name tags
# The [1] tells the program to index into my list at location 1


# Program 2 - better way to code Program 1
if len(sys.argv) < 2: # Checking for errors
    sys.exit("Too few arguments") #sys.exit exits the program prematurely 
elif len(sys.argv) > 2: 
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1]) # By the time the program gets to this line, every error condition has been checked for
# At this point it is safe to assume that there is an item at location [1] in sys.argv