print("main world")

"""
Docstring for Lab9_xenzonz_1
i. LAB 9: Match Coins
ii. Sam Cocquyt
iii. This file runs the game. It creates the Player objects and manages the game loop and rules.
     Implements a "Game Over" state. If a player's wallet reaches 0, the game loop ends automatically, and that player is declared the loser.
iv. No starter code
v. 3/15/2026
"""

from player import Player

def get_play_choice():
    #ask if player wants to play a round
    while True:
        choice = input("toss coins? y/n").strip().lower()

        if choice in ("y", "n"):
            return choice

def play_round():
    return 0 #toss coins

def print_wallets():
    return 0 #print wallets

def final_score_results():
    return 0 #final score and announce winner 

def main() -> None:

    player1: Player = Player("Player 1")
    player2: Player = Player("Player 2")



if __name__ == "__main__":
    main()
