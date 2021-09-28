"""An exercise in remainders and boolean logic."""

__author__ = "730444252"


# Begin your solution here...
number: str = input("Enter an int: ")
if int(number) % 2 == 0:
    if int(number) % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if int(number) % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")