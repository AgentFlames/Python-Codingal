import random

player_choice = int(input("Enter 1 for rock 2 for paper or 3 for scissors: "))
 

if player_choice == 1:
    print("your choice paper: rock")
    player_choice = "ROCK"

elif player_choice == 2: 
    print("your choice : paper")
    player_choice = "PAPER"

elif player_choice == 3:
    print("your choice: scissors")
    player_choice = "SCISSORS"

computer_choice = random.randint(1,3)

if computer_choice == 1:
    print("computer choice paper: rock")
    computer_choice = "ROCK"

elif computer_choice == 2: 
    print("computer choice : paper")
    computer_choice = "PAPER"

elif computer_choice == 3:
    print("computer choice: scissors")
    computer_choice = "SCISSORS"



if computer_choice == player_choice:
    print("Its a draw")

elif computer_choice == "ROCK" and player_choice == "SCISSORS":
    print("computer wins")

elif computer_choice == "PAPER" and player_choice == "ROCK":
    print("computer wins ")

elif computer_choice == "SCISSORS" and player_choice == "PAPER":
    print("computer wins ")

elif player_choice == "ROCK" and computer_choice == "SCISSORS":
    print("player wins")

elif player_choice == "PAPER" and computer_choice == "ROCK":
    print("player wins ")

elif player_choice == "SCISSORS" and computer_choice == "PAPER":
    print("player wins ")