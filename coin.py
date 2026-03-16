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
        #initialize coin object
        self.__sideup: str = random.choice(["heads", "tails"])

    def toss(self) -> None:

        if random.randint(0,1) == 0:
            self.__sideup = "heads"
        else:
            self.__sideup = "tails"

    def get_sideup(self) -> str:

        return self.__sideup
    
def test():

    test_coin = Coin()

    print(test_coin.get_sideup())

    for toss1 in range(1, 10):
        test_coin.toss()
        print(toss1)
        print(test_coin.get_sideup())

test()
