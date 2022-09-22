# Practice programs with the Random Module

# Program 1 - random.choice(seq)
# In random.choice, there is a parameter called seq for sequence
# Sequence stands for something that is a list or list-like
# The choice function from the random module randomly generates a value from a sequence of values
# Below is a simple coin toss program
# By importing random, I am technically importing all the functions that is in that module
import random

# random.choice specifies which function that is associated with the scope of the random module I want to use
coin = random.choice(["heads", "tails"])
print(coin)

# Program 2 - random.choice(seq)
# An alternative (possibly better) approach to importing a library
# Less risk of your code colliding with the variables and functions from the imported library
from random import choice

coin = choice(["heads", "tails"])
print(coin)