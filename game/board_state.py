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