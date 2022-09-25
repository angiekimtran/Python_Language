# Practice programs with the random module

# Program 1 - random.randint(a,b)
# Program that randomly generates an integer between a and b inclusive
# The program below randomly generates a number between 1 and 10
import random

number = random.randint(1, 10)
print(number)

# Program 2 - random.shuffle(x)
# Program that takes in a list of values and shuffles them up to randomize the order they are in
# Below is a card shuffling program
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
