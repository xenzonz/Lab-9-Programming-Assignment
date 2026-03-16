print("player world")

"""
Docstring for Lab9_xenzonz_1
i. LAB 9: Match Coins
ii. Sam Cocquyt
iii. This class represents a player. A player has a name, has a wallet of coins, and has a Coin object to toss.
iv. No starter code
v. 3/15/2026
"""

from coin import Coin

class Player:
    def __init__(self, name: str) -> None:

        self.__name: str = name
        self.__wallet: int = 20
        self.__coin: Coin = Coin()

    def toss_coin(self):
        self.__coin.toss()

    def get_coin_side(self):
        return self.__coin.get_sideup()

    def win_coin(self):
        self.__wallet += 1

    def lose_coin(self):
        self.__wallet -= 1
    
    def get_wallet(self):
        return self.__wallet
    
    def get_name(self):
        return self.__name



def test():
    test_player = Player("player 1")

    print(test_player.get_name())
    print(test_player.get_wallet())
    print(test_player.get_coin_side())

    test_player.toss_coin()
    print(test_player.get_coin_side())

    test_player.win_coin()
    print(test_player.get_wallet())

    test_player.lose_coin()
    print(test_player.get_wallet())

if __name__ == "__main__":
    test()
