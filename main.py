# Rock, Paper, Scissors
# Author:  Ryan Hawkins
# Updated:  2019-11-02

import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


keep_going = True

computer_wins = 0
ties = 0
player_move = ""
moves = ["rock", "paper", "scissors"]
move_dict = {"r": "rock", "p": "paper", "s": "scissors"}


def win():
    global player_wins
    player_wins += 1
    print("You won.")


def play_results():
    if player_move != "q":
        print(f"Player: {player_move} | Computer: {computer_move}")


player_wins = 0

while keep_going:

    player_move = input("""What would you like to do?
(r)ock
(p)aper
(s)cissors
(Q)uit\n""").lower()

    # if player_move == "r":
    #     player_move = "rock"
    # if player_move == "p":
    #     player_move = "paper"
    # if player_move == "s":
    #     player_move = "scissors"

    computer_move = random.choice(moves)

    clear()

    if player_move in ["r", "rock"] and computer_move == "rock":
        print("You tied.")
        ties += 1
    elif player_move in ["r", "rock"] and computer_move == "paper":
        print("You lost.")
        computer_wins += 1
    elif player_move in ["r", "rock"] and computer_move == "scissors":
        win()

    elif player_move in ["p", "paper"] and computer_move == "rock":
        win()
    elif player_move in ["p", "paper"] and computer_move == "paper":
        print("You tie.")
        ties += 1
    elif player_move in ["p", "paper"] and computer_move == "scissors":
        print("You lost.")
        computer_wins += 1

    elif player_move in ["s", "scissors"] and computer_move == "rock":
        print("You lost.")
        computer_wins += 1
    elif player_move in ["s", "scissors"] and computer_move == "paper":
        win()
    elif player_move in ["s", "scissors"] and computer_move == "scissors":
        print("You tie.")
        ties += 1

    elif player_move == "q":
        print("You quit.")
        print(f"Wins:    {player_wins}")
        print(f"Ties:    {ties}")
        print(f"Losses:  {computer_wins}")
        try:
            game_total = player_wins + ties + computer_wins
            win_percentage = (player_wins / game_total) * 100
            print(f"Win Percentage: {round(win_percentage, 1)}%.")
        except:
            pass
        keep_going = False

    else:
        print("\nInvalid input! Try again.\n")
