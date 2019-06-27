import tcod as libtcod
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Entity
from game_messages import MessageLog
from game_states import GameStates
from map_objects.game_map import GameMap
from render_functions import RenderOrder
from loader_functions.constants import get_constants

def get_game_variables(constants):
    constants = get_constants()
    fighter_component = Fighter(hp=constants['player_hp'], defense=constants['player_def'], power=constants['player_pwr'])
    inventory_component = Inventory(26)
    player = Entity(0, 0, constants['player_tile'], libtcod.white, 'Player', blocks=True,
                    render_order=RenderOrder.ACTOR, fighter=fighter_component, inventory=inventory_component)
    entities = [player]

    game_map = GameMap(constants['map_width'], constants['map_height'])
    game_map.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
                      constants['map_width'], constants['map_height'], player, entities,
                      constants['max_monsters_per_room'], constants['max_items_per_room'])

    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])

    game_state = GameStates.PLAYERS_TURN

    return player, entities, game_map, message_log, game_state