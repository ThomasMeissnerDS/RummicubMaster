import game.game_states as game_states
import game.base_classes as base_classes


def sort_stones(play_obj: base_classes.Player = None):
    """
    Function triggers organization of players stones into lists by colours and
    numbers.
    :param play_obj: Instance of Player object.
    :return: Called functions updates class instance.
    """
    play_obj.sort_stones_by_colour()
    play_obj.sort_stones_by_number()


def value_stones(play_obj: base_classes.Player = None):
    """
    Function triggers organization of players stones into lists by colours and
    numbers.
    :param play_obj: Instance of Player object.
    :return: Called functions updates class instance.
    """
    play_obj.value_stones_by_colour()
    play_obj.value_stones_by_number()


def get_value_of_stones_by_number_combinations(play_obj: base_classes.Player = None):
    pass
