#print("main world")

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
    """
    Ask the user if they want to play a round.

    Returns:
        str: The user's validated choice ('y' or 'n').
    """
    while True:
        choice: str = input("Do you want to toss the coins? (y/n): ").strip().lower()

        if choice in ("y", "n"):
            return choice
        
        print("Please enter 'y' or 'n'.")
        

def play_round(player1: Player, player2: Player) -> None:
    """
    Plays a round of the Match Coins game.

    Rules of the game:
        If both coin sides match, Player 1 wins a coin and Player 2 loses one.
        If the coin sides do not match, Player 2 wins a coin and Player 1 loses one.

    Args:
        player1 (Player): The first player.
        player2 (Player): The second player.
    """

    print("\nTossing...")

    player1.toss_coin()
    player2.toss_coin()

    side_player1: str = player1.get_coin_side()
    side_player2: str = player2.get_coin_side()

    print(f"{player1.get_name()} tossed {side_player1}")
    print(f"{player2.get_name()} tossed {side_player2}")

    if side_player1 == side_player2:
        player1.win_coin() #win
        player2.lose_coin() #lose
        print(f"...It's a Match! {player1.get_name()} wins a coin.")
    else:
        player1.lose_coin() #lose
        player2.win_coin() #win
        print(f"...No Match! {player2.get_name()} wins a coin.")



def print_wallets(player1: Player, player2: Player) -> None:
    """
    Print the current number of coins each player has.

    Args:
        player1 (Player): The first player.
        player2 (Player): The second player.
    """
    #player 1
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.") 

    #player 2
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.") 


def final_score_results(player1: Player, player2: Player) -> None:
    """
    Print the final score and announce the winner.

    Args:
        player1 (Player): The first player.
        player2 (Player): The second player.
    """
    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}") 
    print(f"{player2.get_name()}: {player2.get_wallet()}") 

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} finished with more coins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} finished with more coins!")
    else:
        print("Its a draw!")

def main() -> None:
    """
    Runs the Match Coins game.
    """

    player1: Player = Player("Player 1")
    player2: Player = Player("Player 2")

    print("--- Coin Match Game ---")
    print_wallets(player1, player2)
    print()

    choice: str = get_play_choice()

    while choice == "y":
        play_round(player1, player2)
        print()
        print_wallets(player1, player2)

        if player1.get_wallet == 0:
            print("game over! player 1 no money")
            break
        
        if player2.get_wallet == 0:
            print("game over! player 2 no money")
            break

        print()
        choice = get_play_choice()
    
    final_score_results(player1, player2)



if __name__ == "__main__":
    main()
