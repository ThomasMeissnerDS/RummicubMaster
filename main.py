import game.game_states as game_states
import game.base_classes as base_classes


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

    # create bagofstones and fill with stones
    bagofstones = base_classes.BagOfStones(pieces_per_colour=2, nb_jokers=2)
    bagofstones.fill_bag()

    # every player draws starting stones from the bag
    for player_id, player_obj in game_state.players.items():
        stones_drawn = bagofstones.draw_stone(probs.nb_stones_begin)
        player_obj.stones = stones_drawn


if __name__ == '__main__':
    setup_game()
