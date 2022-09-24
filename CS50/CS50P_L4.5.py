# Practice programs with PYPI packages

import cowsay
import sys

# Program 1 - cowsay.cow is a function in the cowsay package that has a cow say something on the screen
# In other words, cowsay produces ASCII art which is a textual way to print pictures on the screen
# Type into the command line terminal the following: python {enter file name} {enter first name}
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1]) #cowsay.cow means I am calling the function cow from the package cowsay

# Program 2 - cowsay.trex is a function in the cowsay package that has a T-Rex say something on the screen
if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])