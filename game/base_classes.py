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
        self.stones_value_by_colour = {}
        self.stones_value_by_number = {}
        self.got_30_out = got_30_out

    def sort_stones_by_colour(self, all_colours=True, chosen_colour=None):
        """
        Takes all stones on players board and organizes them into
        lists of same colour.
        :param all_colours: If True, execute sorting for all colours.
        :param chosen_colour: Only applicable if all_colours is False.
        Expects one of ["red", "blue", "orange", "black"] as a string.
        :return: Updates class instance.
        """
        if all_colours:
            colours = ["red", "blue", "orange", "black"]
        else:
            colours = [chosen_colour]
        for colour in colours:
            self.stones_by_colour[colour] = [s.split("-")[0] for s in self.stones if colour in s]
            self.stones_by_colour[colour].sort()

    def sort_stones_by_number(self, all_numbers=True, chosen_number=None):
        """
        Takes all stones on players board and organizes them into
        lists of same number.
        :param all_numbers: If True, execute sorting for all numbers.
        :param chosen_number: Only applicable if all_numbers is False.
        Expects one of range(1,14) as an integer.
        :return: Updates class instance.
        """
        if all_numbers:
            numbers = [n for n in range(1, 14)]
        else:
            numbers = [chosen_number]
        for num in numbers:
            if len(str(num)) < 2:
                num = "0" + str(num)
            self.stones_by_number[num] = [s.split("-")[0] for s in self.stones if f"{num}" in s]
            self.stones_by_number[num].sort()

    def value_stones_by_colour(self, all_colours=True, chosen_colour=None):
        """
        Takes all stones on players board and calculates the value of them by colour.
        :param all_colours: If True, execute sorting for all colours.
        :param chosen_colour: Only applicable if all_colours is False.
        Expects one of ["red", "blue", "orange", "black"] as a string.
        :return: Updates class instance.
        """
        if all_colours:
            colours = ["red", "blue", "orange", "black"]
        else:
            colours = [chosen_colour]
        for colour in colours:  # TODO: CALCULATE ACTUAL VALUES OF SERIES!!!!
            unique_values = [int(s.split("_")[2].split("-")[0]) for s in set(self.stones) if colour in s]
            self.stones_value_by_colour[colour] = np.sum(np.asarray(unique_values))

    def value_stones_by_number(self, all_numbers=True, chosen_number=None):
        """
        Takes all stones on players board and and calculates the value of them by number.
        :param all_numbers: If True, execute sorting for all numbers.
        :param chosen_number: Only applicable if all_numbers is False.
        Expects one of range(1,14) as an integer.
        :return: Updates class instance.
        """
        if all_numbers:
            numbers = [n for n in range(1, 14)]
        else:
            numbers = [chosen_number]
        for num in numbers:
            if len(str(num)) < 2:
                num = "0" + str(num)
            unique_values = [int(s.split("_")[2].split("-")[0]) for s in set(self.stones) if f"{num}" in s]
            self.stones_value_by_number[num] = np.sum(np.asarray(unique_values))


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
        self.full_unique_id = f"stone_{colour}_{unique_id}-copy_{copy_of_colour}"
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
                    if len(str(piece_no)) < 2:
                        piece_no = "0" + str(piece_no)
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
