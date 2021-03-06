import game.game_states as game_states
import game.base_classes as base_classes
import game.player_actions as player_actions
import operator


def setup_game():
    probs = base_classes.RummiCubProperties(nb_players=4, nb_stones_begin=14)
    game_state = game_states.GameState()

    # create all players
    for player in range(probs.nb_players):
        new_player = base_classes.Player(
                 name=f'player_{player}',
                 unique_id=player,
                 player_type='ai',
                 turn_active=False,
                 stones=None,
                 got_30_out=False)

        # enter players in gamestate register
        game_state.players[new_player.full_unique_id] = new_player

    # define order of players each turn
    game_state.define_order_players()

    # create bagofstones and fill with stones
    bagofstones = base_classes.BagOfStones(pieces_per_colour=2, nb_jokers=2)
    bagofstones.fill_bag()

    # every player draws starting stones from the bag
    for player_id, player_obj in game_state.players.items():
        for piece in range(probs.nb_stones_begin):
            stone_drawn = bagofstones.draw_stone(1)
            player_obj.stones.append(stone_drawn)
            # overwrite current position of stone
            stone_obj = bagofstones.stones_objects[stone_drawn]
            stone_obj.current_position = player_id
            bagofstones.stones_objects[stone_drawn] = stone_obj

    return game_state, bagofstones, probs


def play_game():
    game_state, bagofstones, probs = setup_game()
    # TODO: ADD CHECK IF GAME HAS FINISHED ALREADY FOR WHILE LOOP
    game_state.turn_nb += 1
    curr_turn = game_states.Turn(current_turn=game_state.turn_nb)
    # get turn order
    order_of_players = sorted(game_state.order_of_players.items(), key=operator.itemgetter(1))
    for player, order in order_of_players:
        # store all states at beginning of the turn
        curr_turn.board_state_begin[player] = game_states.BoardState
        curr_turn.player_state_begin[player] = (game_state.players[player]).full_unique_id
        curr_turn.bagofstone_state_begin[player] = bagofstones.stones_left

        # actual execution of the turn
        # sort and evaluate stones of the player
        player_actions.sort_stones(play_obj=game_state.players[player])
        player_actions.value_stones(play_obj=game_state.players[player])
        player_actions.value_stones_by_colour_series(play_obj=game_state.players[player])
        # TODO: ADD FUNCTION WHICH CONSIDERS JOKERS. JOKERS DON'T HAVE A NUMBER AND NEED EXTRA CARE.

        # get all possible actions and take actions as long as desired
        # actions where stones are just placed on board are permutation ids
        # TODO: Add function for getting 30 out actions and their permutations
        # TODO: Add functions to interact with board (get all permutations of board + player board and check if any part is NOT playable)
        # TODO: Add function to just draw (check permutations before and after)
        # TODO: Add function to just clear player board (= win game)


        # store all states at end of the turn
        curr_turn.board_state_end[player] = game_states.BoardState
        curr_turn.player_state_end[player] = (game_state.players[player]).full_unique_id
        curr_turn.bagofstone_state_end[player] = bagofstones.stones_left


if __name__ == '__main__':
    play_game()
