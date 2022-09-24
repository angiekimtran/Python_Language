# Practice programs with command-line arguments, sys.argv, and slice function

import sys

# Program 1 - slices
# To take a slice of a data structure like a list is to take a subset of it
# Type into the command line terminal the following: python {enter file name} {enter n amount of first names}
if len(sys.argv) < 2: 
    sys.exit("Too few arguments") 

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


# Program 2 - slices
if len(sys.argv) < 2: 
    sys.exit("Too few arguments") 

for arg in sys.argv[1:-1]: # Negative numbers has the effect of counting in the other direction from the end of the list.
    print("hello, my name is", arg) # As a result, the last first name entered won't be counted
