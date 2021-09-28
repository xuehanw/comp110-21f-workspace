"""Counting letters in a string."""

__author__ = "73444252"


# Begin your solution here...
letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word: ")
i: int = 0 
count: int = 0
while i <= len(word) - 1:
    if letter == word[i]:
        count = count + 1
        i = i + 1
    else:
        count = count + 0
        i = i + 1

print("Count: " + str(count))