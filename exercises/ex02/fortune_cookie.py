"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730444252"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
i = int(randint(1, 60))
if i >= 50:
    print("A beautiful and smart loving person will be coming into your life.")
else:
    if i > 25:
        print("Your life will be happy.")
    else:
        if i > 10:
            print("You life will be peaceful.")
        else:
            print("Soon life will become more interesting.")
print("Now, go spread positive vibes!")
