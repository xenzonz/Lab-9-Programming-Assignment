print("player world")

"""
Docstring for Lab9_xenzonz_1
i. LAB 9: Match Coins
ii. Sam Cocquyt
iii. Player code
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
        return self.__coin.get_sideup

    def win_coin(self):
        return 0

    def lose_coin(self):
        return 0
    
    def get_wallet(self):
        return 0
    
    def get_name(self):
        return 0



