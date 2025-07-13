import random

options = ("rock" ,"paper" ,"scissor")

name = input("Enter your name: ")
player = None

is_running = True
while is_running :
    computer = random.choice(options)
    player = input("Enter your choice[rock,paper,scissor]: ")
    print(f"player: {player}")
    print(f"computer: {computer}")

    if(player == "rock" and computer == "scissor"):
        print("PLAYER WINS")
    elif(player == "scissor" and computer == "paper"):
        print("PLAYER WINS")
    elif(player == "paper" and computer == "rock"):
        print("PLAYER WINS")
    elif(player == "rock" and computer == "paper"):
        print("COMPUTER WINS")
    elif(player == "scissor" and computer == "rock"):
        print("COMPUTER WINS")
    elif(player == "paper" and computer == "scissor"):
        print("COMPUTER WINS")
    elif(player == computer):
        print("TIE")
    else:
        print("INVALID INPUT BY PLAYER")
    

    X = input("you want to play again? ")
    if X == "no":
        is_running = False
        print(f"THANKS FOR PLAYING {name}")
    else:
        is_running = True
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
