"""Example of a function that processes a list."""
# To test the funciton below
def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))

# Define a function named contains
# We can give the arguments: a needle value we're searching for in a haystack list
def contains(needle: str, haystack: list[str]) -> bool:
    """Return true if needle is found in haystack, false otherwise.""" 
    # Loop through each index in list
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
        # Test if item stored at index in equal to needle
        # Return true if so
            return True
        i += 1
    # Return false after testing each item 
    return False

if __name__ == "__main__":
    main()