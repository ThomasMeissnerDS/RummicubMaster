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
    :param unique_id: Unique id of this player.
    :param player_type: 'human' will require manual imput for this player while
    'ai' will let artificial intelligence decide on all moves.
    :param stones: List containing all stones a player currently has.
    :param got_30_out: Boolean flagging if the player already placed the first 30 points
    on the board.
    """
    def __init__(self,
                 name: str = 'Thomas',
                 unique_id: int = 0,
                 player_type: str = 'ai',
                 turn_active: bool = False,
                 stones=None,
                 got_30_out: bool = False):
        self.name = name
        self.short_unique_id = unique_id
        self.full_unique_id = f"player_{unique_id}"
        self.player_type = player_type
        self.turn_active = turn_active
        if isinstance(stones, list):
            self.stones = stones  # expects a list
        else:
            self.stones = []
        self.stones_by_colour = {}
        self.stones_by_number = {}
        self.got_30_out = got_30_out

    def sort_stones_by_colour(self):
        """
        Takes all stones on players board and organizes them into
        lists of same colour.
        :return: Updates class instance.
        """
        self.stones_by_colour["red"] = [s for s in self.stones if "red" in s]
        self.stones_by_colour["red"].sort()
        self.stones_by_colour["blue"] = [s for s in self.stones if "blue" in s]
        self.stones_by_colour["blue"].sort()
        self.stones_by_colour["orange"] = [s for s in self.stones if "orange" in s]
        self.stones_by_colour["orange"].sort()
        self.stones_by_colour["black"] = [s for s in self.stones if "black" in s]
        self.stones_by_colour["black"].sort()

    def sort_stones_by_number(self):
        """
        Takes all stones on players board and organizes them into
        lists of same number.
        :return: Updates class instance.
        """
        for num in range(1, 14):
            self.stones_by_number[num] = [s for s in self.stones if f"{num}" in s]
            self.stones_by_number[num].sort(

            )


class Stone:
    """
    Base class for all stones. Holds properties including current position of each stone.
    :param unique_id: Integer which will be unique in combination with other properties.
    """
    def __init__(self,
                 unique_id: int = 0,
                 colour: str = None,
                 copy_of_colour: int = 0,
                 is_joker: bool = False,
                 position: str = None):
        self.unique_id = unique_id
        self.short_unique_id = f"{colour}_{unique_id}"
        self.full_unique_id = f"stone_{colour}_{copy_of_colour}_{unique_id}"
        self.colour = colour
        self.copy_of_colour = copy_of_colour
        self.is_joker = is_joker
        self.current_position = position


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
        self.full_unique_id = "bagofstones"
        self.stones_objects = {}

    def fill_bag(self):
        """
        Function to fill the bag with all stones at the beginning of the game.
        :return:
        """
        self.stones_left = []
        for i in range(self.pieces_per_colour):
            for col in ["red", "blue", "orange", "black"]:
                for piece_no in range(1, 14):
                    stone = Stone(unique_id=piece_no,
                                  colour=col,
                                  copy_of_colour=i,
                                  is_joker=False,
                                  position="bagofstones")
                    self.stones_objects[stone.full_unique_id] = stone
                    self.stones_left.append(stone.full_unique_id)

        for i in range(self.nb_jokers):
            stone = Stone(unique_id=i,
                          colour="joker",
                          copy_of_colour=i,
                          is_joker=True,
                          position="bagofstones")
            self.stones_objects[stone.full_unique_id] = stone
            self.stones_left.append(stone.full_unique_id)

    def draw_stone(self, nb_to_draw: int = 1):
        """
        Draws a stone from the bag, removes the stones from
        the bag and returns the drawn stone.
        :param nb_to_draw: Number of stones to draw from the bag.
        :return: Full unique id of the stone.
        """
        stones = np.random.choice(self.stones_left, size=nb_to_draw, replace=False)
        for stone in stones:
            self.stones_left.remove(stone)
        return stones[0]  # return only the element not a numpy array
