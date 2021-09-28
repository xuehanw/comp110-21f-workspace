"""Project1."""

__author__ = "730444252"

from random import randint
points: int = 0
player: str = ""

CONSTANT: int = 6
CONGRATS: str = "\U0001F389"


def main() -> None:
    """A main function."""
    global points
    global player
    points = 0
    player = ""
    greet()
    i: int = 0
    while i == 0:
        next: str = input("Are you sure you want to start this game? Enter 'yes', 'no' or 'maybe': ")
        if next == "no":
            print(f"Your point it {points}. Goodbye, {player}!")
            break
        else:
            if next == "maybe":
                print(f"{player}, you will like this game, trust me!!!")
    # the first step
        print(f"{player}, there are two doors, a red door and a yellow door, in front of you, which whould you like to enter? ")
        door: str = input("Enter 'r' for the red door, 'y' for the yellow door or 'q' to quit the game: ")
        print(firstdoor(door))
    # the second step 
        print(f"Then, {player}, choose you lucky number form 1 to 9")
        luckyn: str = input("Enter here: ")
        print("Points:", end="")
        print(secondstep(int(luckyn)))
    # the third step 
        print(f"You are almost there! {CONGRATS}")
        print("If you can only bring one thing with you to another planet, what will you choose: flower, food, or phone?")
        onething: str = input("Enter 'f' for flower, 'fo' for food, or 'p' for phone: ")
        print(thirdstep(onething))
    # mysterious box
        print("Good News: you have found a mysterious box behind the door!!!")
        print("The probability that there are extra points in the box is greater than that the box have evil beings that can swallow your points.")
        print(scores(points))
        if points <= 0:
            print(f"{CONGRATS}{player}, you are a Fire-type pokemon like Torchic, Cyndaquil, or Charmander!!!")
        else:
            if points <= 10:
                print(f"{CONGRATS}{player}, you are an electric-type pokemon like Pikachu!!!")
            else:
                print(f"{CONGRATS}{player}, you are a water-type pokemon like Psyduck, Totodile, Mudkip, or Squirtle!!!")
    # game loop
        loop: str = input("Restart the pokemon game? Enter 'restart' or 'quit': ")
        if loop == "restart":
            i = i + 0
            print(f"You total score is {points}.")
        else:
            print(f"Your point is {points}. Goodbye {player}!")
            i = i + 1
            

def greet() -> None:
    """A greet procedure."""
    global player
    player = input("What is your name? ")
    print(f"Hi {player}")
    print("Welcome!")
    print("When you open your eyes in the morning, you find yourself turned into a pokemon.")
    print("Ever wonder what pekemon are you? Play this game!")


def firstdoor(x: str) -> str:
    """The game procedure."""
    global points
    if x == "r":
        points = 1
        print(f"{CONGRATS} You have opened the Door of Courage!")
    else:
        x == "y"
        points = 2
        print(f"{CONGRATS} You have opened the Door of Honest!")
    return (f"Points: {points}")


def secondstep(x: int) -> int:
    """This is the secondstep."""
    global points
    if x < 6:
        points = points + 1
    else:
        if x == CONSTANT:
            points = points + 3
        else:
            points = points + 2
    return(points)


def thirdstep(x: str) -> str:
    """This is the third step."""
    global points
    if x == "f":
        points = points + 5
    else:
        if x == "fo":
            points = points + 3
        else:
            points = points + 1
    return (f"Points: {points}")


def scores(x: int) -> int:
    """Socre report."""
    global points
    box: str = input("Do you want to open this box? Enter 'open' or 'ignore': ")
    if box == "open":
        points = x + randint(-5, 9)
    else:
        return x
    print(f"Now, {player}, your total point is: ", end="")
    return x


if __name__ == "__main__":
    main()