"""An exercise in remainders and boolean logic."""

__author__ = "730411656"


# Begin your solution here...
how_much: int = int(input("Enter an int: "))

if how_much % 7 == 0 and how_much % 2 == 0:
    print("TAR HEELS")
else:
    if how_much % 2 == 0:
        print("TAR") 
    else:
        if how_much % 7 == 0:
            print("HEELS")
        else: 
            print("CAROLINA")
