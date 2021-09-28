"""Repeating a beat in a loop."""

__author__ = "730444252"


# Begin your solution here...
beat: str = input("What beat do you want to input? ")
counter: int = 1
repeat_times: int = int(input("How many times do you want to repeat it? "))
if repeat_times > 0:
    while counter <= repeat_times:
        if counter < repeat_times:
            print(beat, end=" ")
        else:
            print(beat)
        counter = counter + 1
        
else:

    print("No beat...")
