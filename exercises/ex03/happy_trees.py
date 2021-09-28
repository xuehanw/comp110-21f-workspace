"""Drawing forests in a loop."""

__author__ = "730444252"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: str = input("Depth: ")
i: int = 0
while i < int(depth):
    print(TREE * (i + 1))
    i = i + 1
