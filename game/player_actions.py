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


def value_stones_by_colour_series(play_obj: base_classes.Player = None):
    """
    Function triggers evaluation of players' stones into multiple dictionaries wih permutation_id as key.
    :param play_obj: Instance of Player object.
    :return: Called functions updates class instance.
    """
    play_obj.value_stones_by_colour_series()


def permutations_play_by_number(props: base_classes.RummiCubProperties = None):
    """
    Function calculates all possible play permutations a player could play.
    These permutations are standalone sets of stones and are just put on board.
    They are played technically regardless of the board state. These permutations
    require at least 3 stones and there can't be more jokers than non-jokers within.
    :param bag_obj:
    :return:
    """
    colour_combinations = []
    for colour_a in props.colours:
        for colour_b in props.colours:
            for colour_c in props.colours:
                for colour_d in props.colours:
                    temp_list = [colour_a, colour_b, colour_c, colour_d]
                    comb = set(temp_list)
                    if len(list(comb)) < 3:
                        pass
                    else:
                        if comb in colour_combinations:
                            pass
                        else:
                            colour_combinations.append(comb)

    colour_number_combinations = []
    for number in range(1, 14):
        if number < 10:
            number = "0"+str(number)
        for part in colour_combinations:
            temp_comb = []
            for colour in part:
                temp_comb.append(str(colour)+"_"+str(number))
            colour_number_combinations.append(temp_comb)


def permutations_append_by_number(props: base_classes.RummiCubProperties = None):
    """
    Function calculates all possible permutations a player could play.
    These permutations are me<nt for appending the stones onto already existing sets on the board.
    These permutation can be of any size.
    :param bag_obj:
    :return:
    """
    pass



