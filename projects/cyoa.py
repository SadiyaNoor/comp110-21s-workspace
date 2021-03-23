"""Choose Your Own Adventure."""

__author__ = "730411656"
from random import randint

player: str
points: int = int(0)
attempts: int = int(5)
emoji: str = " \U0001F911"
title: str = str(f"Coin Game{ emoji}")


def main() -> None: 
    """Carries out entirety of the game."""
    greet()
    userchoice = input("Would you like to play easy, medium, or just quit? ")
    if userchoice == "easy":
        print("Wow you chose easy? If you lose it will be super pathetic.")
        print(easy())
    else:
        if userchoice == "medium":
            print("Medium difficulty huh? I see you have some self confidence.")
            print(medium())
        else:
            print("Bruh I spent hours on this and you didnt even try...bye :/") 
            exit()


def greet() -> None:
    """The start screen where name is define."""
    global player
    global title
    player = input("Name: ")
    print(f"Welcome to the { title} {player}!")
    print("To win the game, guess the coin flip enough of out 5 tries correctly.")
    return None


def easy() -> str:
    """Easy version of the game with head or tails."""
    global points
    global title
    global player
    i: int = 0
    tries: int = 5
    # 1. the actual function of the points, win/lose
    while i < tries:
        answer = randint(1, 2)
        playerguess = str(input("Heads or Tails? For heads type H, for tails type T: "))
        # 2. this assigns H or T to a number since randstr isnt a thing
        if playerguess == "H":
            playerguessnum = 1
        else:
            playerguessnum = 2

        if answer == playerguessnum:
            points += 1
            i += 1
            if points == 3:
                return(f"You won the {title} with {points} points, good job {player}!")
        else:
            if answer != playerguessnum:
                i += 1
    return(f"You lost with {points} out of 5, sorry {player}!")
    

def medium() -> str:
    """Harder version of the game with Head, tails, or side."""
    global points
    global title
    global player
    i: int = 0
    tries: int = 5
    # 1. the actual function of the points, win/lose
    while i < tries:
        playerguess = input("Heads, tails or side? For heads type H, for tails type T and for side type S: ")
        answer = randint(1, 3)
        if playerguess == "H":
            playerguessnum = 1
        else:
            if playerguess == "T":
                playerguessnum = 2
            else:
                playerguessnum = 3
        if answer == playerguessnum:
            points += 1
            i += 1
            if points == 3:
                return(f"You won the {title}, good job {player}!")
        else:
            if answer != playerguessnum:
                i += 1
    return(f"You lost with {points} points, sorry {player} but you suck lol!")


if __name__ == "__main__":
    main()