import tcod as libtcod
from render_functions import RenderOrder
from game_states import GameStates
from game_messages import Message
from loader_functions.constants import get_constants

constants = get_constants()

def kill_player(player):
    player.char = constants['player_tile']
    player.color = libtcod.dark_red

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = constants['orc_tile']
    if monster.name == 'Troll':
        monster.char = constants['troll_tile']
    elif monster.name == 'Orc':
        monster.char = constants['orc_tile']
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE
    monster.dead = True

    return death_message