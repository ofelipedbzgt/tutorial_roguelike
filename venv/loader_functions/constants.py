import tcod as libtcod

def get_constants():
    window_title = 'Roguelike Tutorial Revised'
    font_file = 'TiledFont16x16.png'
    font_file_menu = 'arial10x10.png'

    main_menu_background_image = 'menu_background.png'

    screen_width = 84
    screen_height = 42

    map_width = 83
    map_height = 36

    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height

    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    room_max_size = 11
    room_min_size = 6
    max_rooms = 32

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    max_monsters_per_room = 3
    max_items_per_room = 3

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

    player_hp = 60
    player_def = 2
    player_pwr = 5

    orc_hp = 10
    orc_def = 0
    orc_pwr = 3

    troll_hp = 16
    troll_def = 1
    troll_pwr = 4

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50)
    }

    constants = {
        'window_title': window_title,
        'font_file': font_file,
        'font_file_menu': font_file_menu,
        'main_menu_background_image': main_menu_background_image,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'bar_width': bar_width,
        'panel_height': panel_height,
        'panel_y': panel_y,
        'message_x': message_x,
        'message_width': message_width,
        'message_height': message_height,
        'map_width': map_width,
        'map_height': map_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'colors': colors,
        'wall_tile': wall_tile,
        'floor_tile': floor_tile,
        'player_tile': player_tile,
        'orc_tile': orc_tile,
        'troll_tile': troll_tile,
        'scroll_tile': scroll_tile,
        'healingpotion_tile': healingpotion_tile,
        'sword_tile': sword_tile,
        'shield_tile': shield_tile,
        'stairsdown_tile': stairsdown_tile,
        'dagger_tile': dagger_tile,
        'player_hp': player_hp,
        'player_def': player_def,
        'player_pwr': player_pwr,
        'orc_hp': orc_hp,
        'orc_def': orc_def,
        'orc_pwr': orc_pwr,
        'troll_hp': troll_hp,
        'troll_def': troll_def,
        'troll_pwr': troll_pwr
    }

    return constants