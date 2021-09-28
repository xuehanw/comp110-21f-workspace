"""numeric-operators exercises."""
__author__ = "730444252"
left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
a = int(left) ** int(right)
b = int(left) / int(right)
c = int(left) // int(right)
d = int(left) % int(right)
print(left + " ** " + right + " is " + str(a))
print(left + " / " + right + " is " + str(b))
print(left + " // " + right + " is " + str(c))
print(left + " % " + right + " is " + str(d))