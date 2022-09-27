# Practice program building custom libraries (Part 2)

import sys # So that I can have access to command-line arguments

from CS50P_L4_7 import hello # Because I created a file titled "CS50P_L4_7", I can import a function from the module that I created in that file

if len(sys.argv) == 2: # If the user obliges by entering two command-line arguments (the file name and person's name) which I can check through sys.argv, then the program will call on the function "hello(sys.argv[1])"
    hello(sys.argv[1])