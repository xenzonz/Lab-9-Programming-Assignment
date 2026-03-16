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

def get_play_choice() -> str:
    #ask if player wants to play a round
    while True:
        choice: str = input("toss coins? y/n").strip().lower()

        if choice in ("y", "n"):
            return choice

def play_round(player1: Player, player2: Player) -> None:
    
    #if both coins match, player1 wins a coin, player2 loses a coin
    #if no coins match, player1 loses a coin, player2 wins a coin

    player1.toss_coin()
    player2.toss_coin()

    side_player1: str = player1.get_coin_side()
    side_player2: str = player2.get_coin_side()

    print(f"{player1.get_name()} tossed {side_player1}")
    print(f"{player2.get_name()} tossed {side_player2}")

    if side_player1 == side_player2:
        player1.win_coin() #win
        player2.lose_coin() #lose
        print(f"matched, {player1.get_name()} wins a coin")
    else:
        player1.lose_coin() #lose
        player2.win_coin() #win
        print(f"no match, {player2.get_name()} wins a coin")



def print_wallets(player1: Player, player2: Player) -> None:

    #player 1
    print(f"{player1.get_name()} has {player1.get_wallet()} coins") 

    #player 2
    print(f"{player2.get_name()} has {player2.get_wallet()} coins") 

def final_score_results(player1: Player, player2: Player):
    return 0 #final score and announce winner 

def main() -> None:

    player1: Player = Player("Player 1")
    player2: Player = Player("Player 2")



if __name__ == "__main__":
    main()
