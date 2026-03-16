#print("player world")

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
    """
    Represent a player in the Match Coins game.

    Attributes:
        __name (str): The player's name.
        __wallet (int): The number of coins the player has.
        __coin (Coin): The player's coin object.
    """
    def __init__(self, name: str) -> None:
        """
        Initialize a Player object.

        Args:
            name (str): The name of the player.
        """
        self.__name: str = name
        self.__wallet: int = 20
        self.__coin: Coin = Coin()

    def toss_coin(self) -> None:
        """
        Tell the player's coin to toss itself.
        """
        self.__coin.toss()

    def get_coin_side(self) -> str:
        """
        Get the current side of the player's coin.

        Returns:
            str: The current side of the player's coin.
        """
        return self.__coin.get_sideup()

    def win_coin(self) -> None:
        """
        Add one coin to the player's wallet.
        """
        self.__wallet += 1

    def lose_coin(self) -> None:
        """
        Subtract one coin from the player's wallet.
        """
        self.__wallet -= 1
    
    def get_wallet(self) -> int:
        """
        Return the number of coins in the player's wallet.

        Returns:
            int: The current number of coins in the wallet.
        """
        return self.__wallet
    
    def get_name(self) -> str:
        """
        Return the player's name.

        Returns:
            str: The player's name.
        """
        return self.__name

#test code
"""
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
"""
