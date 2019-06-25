import tcod as libtcod
from render_functions import RenderOrder
from game_states import GameStates
from game_messages import Message

wall_tile = 256
floor_tile = 257
player_tile = 258
orc_tile = 259
troll_tile = 260
scroll_tile = 261
healingpotion_tile = 262
sword_tile = 263
shield_tile = 264
stairsdown_tile = 265
dagger_tile = 266

def kill_player(player):
    player.char = player_tile
    player.color = libtcod.dark_red

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = orc_tile
    if monster.name == 'Troll':
        monster.char = troll_tile
    elif monster.name == 'Orc':
        monster.char = orc_tile
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message