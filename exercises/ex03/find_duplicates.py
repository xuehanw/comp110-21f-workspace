"""Finding duplicate letters in a word."""

__author__ = "730444252"


word: str = input("Enter a word: ")


def finddup(word: str) -> None:
    """Find duplicates."""
    i: int = 0
    count: int = 0
    while i < len(word):
        j: int = i + 1
        while j < (len(word)):
            if word[i] == word[j]:
                count = count + 1
                j = j + 1
            else:
                j = j + 1
        i = i + 1
    if count > 0: 
        print("Found duplicate: True")
    else:
        print("Found duplicate: False")


finddup(word)
