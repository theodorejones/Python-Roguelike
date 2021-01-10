#!/usr/bin/env python
import libtcodpy as tcod
import sqlite3
from random import seed
from random import randint

#Setup a field into which to insert values
field=[]
x_field = 4
y_field = 4
for y in range(y_field):
    field.append([])
    for x in range(x_field):
        field[y].append(1)

FULLSCREEN = False
SCREEN_WIDTH = 80  # characters wide
SCREEN_HEIGHT = 50  # characters tall
LIMIT_FPS = 20  # 20 frames-per-second maximum
# Game Controls
TURN_BASED = True  # turn-based game

def get_key_event(turn_based=None):
    if turn_based:
        # Turn-based game play; wait for a key stroke
        key = tcod.console_wait_for_keypress(True)
    else:
        # Real-time game play; don't wait for a player's key stroke
        key = tcod.console_check_for_keypress()
    return key
 
def handle_keys():
    global player_x, player_y
    global field, x_field, y_field
    
    key = get_key_event(TURN_BASED)
 
    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
 
    
    # movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        if(player_y > 0):
            field[player_x][player_y]=0
            player_y -= 1
            field[player_x][player_y]=2
 
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        if(player_y < y_field - 1):
            field[player_x][player_y]=0
            player_y += 1
            field[player_x][player_y]=2
        
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        if(player_x > 0):
            field[player_x][player_y]=0
            player_x -= 1
            field[player_x][player_y]=2
 
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        if(player_x < x_field - 1):
            field[player_x][player_y]=0
            player_x += 1
            field[player_x][player_y]=2

def main():
    # Setup player
    global player_x, player_y
    player_x = x_field // 2
    player_y = y_field // 2
    field[player_x][player_y] = 2
    # Setup Font
    font_filename = 'dejavu10x10_gs_tc.png'
    tcod.console_set_custom_font(font_filename, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
 
    # Initialize screen
    title = 'DeliverRogue'
    tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, title, FULLSCREEN)
 
    # Set FPS
    tcod.sys_set_fps(LIMIT_FPS)
 
    exit_game = False
    while not tcod.console_is_window_closed() and not exit_game:
        tcod.console_set_default_foreground(0, tcod.white)
        for y in range(y_field):
            for x in range(x_field):
                if(field[x][y] == 2):
                    tcod.console_put_char(0, player_x, player_y, '@', tcod.BKGND_NONE)
                else:
                    tcod.console_put_char(0, x, y, field[x][y], tcod.BKGND_NONE)
        tcod.console_flush()
        #tcod.console_put_char(0, player_x, player_y, ' ', tcod.BKGND_NONE)
        for y in range(y_field):
            for x in range(x_field):
                if(field[x][y] == 2):
                    tcod.console_put_char(0, player_x, player_y, '@', tcod.BKGND_NONE)
                else:
                    tcod.console_put_char(0, x, y, field[x][y], tcod.BKGND_NONE)
 
        exit_game = handle_keys()
 
 
main()
