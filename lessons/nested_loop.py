"""example of a nested loop."""

word: str = input("Enther a word: ")

i: int = 0
while i < len(word):
    j: int = 0
    while j < len(word):
        print(word[j])
        j = j + 1
    i = i + 1