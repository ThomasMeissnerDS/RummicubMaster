import numpy as np


class RummiCubProperties:
    """
    Start properties of each game.
    :param nb_players: Number of players in the game.
    :param nb_stones_begin: Number of stones each player has to draw from the bag of stones.
    """
    def __init__(self,
                 nb_players: int = 4,
                 nb_stones_begin: int = 14):
        self.nb_players = nb_players
        self.nb_stones_begin = nb_stones_begin


class Player:
    """
    Player class containing properties of a player.
    :param name: Name of the player (optional).
    :param stones: List containing all stones a player currently has.
    :param got_30_out: Boolean flagging if the player already placed the first 30 points
    on the board.
    """
    def __init__(self,
                 name: str = 'Thomas',
                 turn_active: bool = False,
                 stones=None,
                 got_30_out: bool = False):
        self.name = name
        self.turn_active = turn_active
        self.stones = stones  # expects a list
        self.got_30_out = got_30_out


class BagOfStones:
    """
    Bag containing all the stones (left).
    :param pieces_per_colour: Number of times the sme stones occurs per colour.
    :param stones_left: List containing all stomes left in the bag. Needs to be filled with
    fill_bag method at first.
    Defaults as 2.
    """
    def __init__(self,
                 pieces_per_colour: int = 2,
                 nb_jokers: int = 2,
                 stones_left=None):
        self.stones_left = stones_left
        self.pieces_per_colour = pieces_per_colour
        self.nb_jokers = nb_jokers

    def fill_bag(self):
        """
        Function to fill the bag with all stones at the beginning of the game.
        :return:
        """
        self.stones_left = []
        for i in range(self.pieces_per_colour):
            for col in ["red", "blue", "orange", "black"]:
                stones = [col+f"_{i+1}" for i in range(13)]
                for piece in stones:
                    self.stones_left.append(piece)

        for i in range(self.nb_jokers):
            self.stones_left.append("joker")

    def draw_stone(self, nb_to_draw: int = 1):
        """
        Draws a stone from the bag, removes the stones from
        the bag and returns the drawn stone.
        :param nb_to_draw: Number of stones to draw from the bag.
        :return:
        """
        stones = np.random.choice(self.stones_left, size=nb_to_draw)
        self.stones_left.remove(stones)
        return stones
