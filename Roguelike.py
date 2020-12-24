#!/usr/bin/env python
import libtcodpy as tcod
import sqlite3

#Opening database

conn = sqlite3.connect('test.db')

print ("Opened database successfully")

#Request username, for now represented by a simple text input

name = input("Please supply a username: ")

#Final product will have four save slots

try:
    conn.execute('''CREATE TABLE PLAYERONE
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT     NOT NULL,
         X            INT     NOT NULL,
         Y            INT     NOT NULL,
         HEALTH            INT     NOT NULL);''')
except:
    print("Welcome Back!")
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
 
    key = get_key_event(TURN_BASED)
 
    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
 
    elif key.vk == tcod.KEY_ESCAPE:
        return True  # exit game
 
    # movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_y -= 1
 
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_y += 1
 
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_x -= 1
 
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_x += 1
 
def main():
    # Setup player
    global player_x, player_y
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
 
    # Setup Font
    font_filename = 'dejavu10x10_gs_tc.png'
    tcod.console_set_custom_font(font_filename, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
 
    # Initialize screen
    title = 'Python 3 + Libtcod tutorial'
    tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, title, FULLSCREEN)
 
    # Set FPS
    tcod.sys_set_fps(LIMIT_FPS)
 
    exit_game = False
    while not tcod.console_is_window_closed() and not exit_game:
        tcod.console_set_default_foreground(0, tcod.white)
        tcod.console_put_char(0, player_x, player_y, '@', tcod.BKGND_NONE)
        tcod.console_flush()
        tcod.console_put_char(0, player_x, player_y, ' ', tcod.BKGND_NONE)
        str_x=str(player_x)
        str_y=str(player_y)
        conn.execute("INSERT INTO PLAYERONE (ID,X,Y,HEALTH) \
      VALUES (20, "+str_x+", "+str_y+", 40 )")
 
        exit_game = handle_keys()
 
 
main()
