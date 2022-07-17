import numpy as np


class GameState:
    """
    Class holding information about current game state.
    :param active_player: Unique ID of player who is currently on turn.
    :param turn_nb: Number of the active turn.
    :param game_finished: Marks if game is finished or ongoing.
    :param game_log: Dictionary holding all event data.
    """
    def __init__(self,
                 active_player: str = None,
                 turn_nb: int = 0,
                 game_finished: bool = False,
                 game_log=None):
        self.turn_nb = turn_nb
        self.turns = []
        self.players = {}
        self.order_of_players = {}
        self.active_player = active_player
        self.game_finished = game_finished
        self.game_log = game_log

        if isinstance(game_log, dict):
            self.game_log = game_log
        else:
            self.game_log = {}
            self.game_log["turn"] = {}

    def define_order_players(self):
        """
        Randomly assigns order of players within each turn.
        :return: Updates class attribute
        """
        player_list = []
        for pl_id, pl_obj in self.players.items():
            player_list.append(pl_id)

        for order in range(len(player_list)):
            player = np.random.choice(player_list, size=1, replace=False)
            self.order_of_players[player[0]] = order
            player_list.remove(player[0])


class BoardState:
    """
    Class holding information about the current board.
    :param nb_formations: Number of stone formations currently placed on the board.
    :param pieces_per_colour: Number of times the sme stones occurs per colour.
    Should match same attribute from BagOfStones class.
    """
    def __init__(self,
                 nb_formations: int = 0,
                 pieces_per_colour: int = 2):
        self.nb_formations = nb_formations
        self.pieces_per_colour = pieces_per_colour
        self.board_matrices = {"red": None,
                               "blue": None,
                               "orange": None,
                               "black": None,
                               "mixed": None}


class Turn:
    """
    Class holding information of each turn. Stores state at beginning and end of each turn.
    States are stored as dictionaries representing each player key-wise.
    """
    def __init__(self,
                 current_turn: int = 0):
        self.current_turn = current_turn
        self.board_state_begin = {}
        self.board_state_end = {}
        self.bagofstone_state_begin = {}
        self.bagofstone_state_end = {}
        self.player_state_begin = {}
        self.player_state_end = {}
