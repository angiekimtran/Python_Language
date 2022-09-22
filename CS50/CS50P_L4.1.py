# Practice programs with the Random Module

# Program 1
# Coin toss program
# By importing random, I am technically importing everything that is in that module
import random

# random.choice specifies which function that is associated with the scope of the random module I want to use
coin = random.choice(["heads", "tails"])
print(coin)

# Program 2
# An alternative (possibly better) approach to importing a library
# Less risk of your code colliding with the variables and functions from the imported library
from random import choice

coin = choice(["heads", "tails"])
print(coin)