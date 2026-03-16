print("coin world")

"""
Docstring for Lab9_xenzonz_1
i. LAB 9: Match Coins
ii. Sam Cocquyt
iii. Coin code
iv. No starter code
v. 3/15/2026
"""

import random

class Coin:
    
    def __init__(self) -> None:
        #initialize coin object, head side up by default
        self.__sideup: str = "heads"

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "heads"
        else:
            self.__sideup = "tails"

    def get_sideup(self):
        return self.__sideup

print(Coin)