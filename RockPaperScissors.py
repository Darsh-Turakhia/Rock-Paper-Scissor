from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors","Rock", "Paper", "Scissors","Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,8)]

#set player to False
player = False

while player == False:
    computer = t[randint(0,8)]
    player = input("\n Rock, Paper, Scissors ? (Type q to exit) ")
    if player == computer:
        print("Tie!")
        player = False
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            player = False
        else:
            print("You win!", player, "smashes", computer)
            player = False
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            player = False
        else:
            print("You win!", player, "covers", computer)
            player = False
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            player = False
        else:
            print("You win!", player, "cut", computer)
            player = False
    elif player == "q":
        print("\n Exiting .... ")
        player = True
    else:
        print("That's not a valid play. Check your spelling!")
        player = False
