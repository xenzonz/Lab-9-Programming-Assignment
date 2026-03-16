#print("coin world")

"""
Docstring for Lab9_xenzonz_1
i. LAB 9: Match Coins
ii. Sam Cocquyt
iii. This class represents a single, tossable coin. It only knows about its own state (heads or tails).
iv. No starter code
v. 3/15/2026
"""

import random

class Coin:
    """
    Represent a single coin that can be tossed.

    Attributes:
        __sideup (str): The current side of the coin, either 'Heads' or 'Tails'.
    """
    def __init__(self) -> None:
        """
        Initialize a Coin object.

        The coin starts with a random side facing up.
        """
        self.__sideup: str = random.choice(["heads", "tails"])

    def toss(self) -> None:
        """
        Toss the coin and randomly set it to Heads or Tails.
        """
        if random.randint(0,1) == 0:
            self.__sideup = "heads"
        else:
            self.__sideup = "tails"

    def get_sideup(self) -> str:
        """
        Return the side of the coin that is currently facing up.

        Returns:
            str: The current side of the coin.
        """
        return self.__sideup

#test code 
"""
def test():

    test_coin = Coin()

    print(test_coin.get_sideup())

    for toss1 in range(1, 10):
        test_coin.toss()
        print(toss1)
        print(test_coin.get_sideup())

if __name__ == "__main__":
    test()
"""