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
        self.active_player = active_player
        self.game_finished = game_finished
        self.game_log = game_log

        if isinstance(game_log, dict):
            self.game_log = game_log
        else:
            self.game_log["turn"] = {}


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
