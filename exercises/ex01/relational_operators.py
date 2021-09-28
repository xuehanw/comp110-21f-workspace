"""relational-operators exercises."""
__author__ = "730444252"
left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
a = bool(int(left) < int(right))
b = bool(int(left) >= int(right))
c = bool(int(left) == int(right))
d = bool(int(left) != int(right))
print(left + " < " + right + " is " + str(a))
print(left + " >= " + right + " is " + str(b))
print(left + " == " + right + " is " + str(c))
print(left + " != " + right + " is " + str(d))