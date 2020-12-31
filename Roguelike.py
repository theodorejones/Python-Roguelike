#!/usr/bin/env python
import libtcodpy as tcod
import sqlite3
from random import seed
from random import randint

#Opening database

conn = sqlite3.connect('test.db')

print ("Opened database successfully")

#Setup variables for score handling based on steps taken to progress
score = 0
buffer = 0

#Setup a field into which to insert values
field=[]
x_field = 20
y_field = 20
for y in range(y_field):
    field.append([])
    for x in range(x_field):
        field[y].append(1)

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
    global player_x, player_y, score, buffer
    global field, x_field, y_field
 
    key = get_key_event(TURN_BASED)
 
    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
 
    
    # movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        field[player_x][player_y]=0
        if(buffer == 0):#If the next step takes the character further up the map
            score= score + 1
            field.pop()#Remove last row
            row = []#Create next row
            for x in range(x_field):
                row.append(1)
            for x in range(20):#Generate next row
                value = randint(0, x_field - 1)
                row[value] = row[value]+1
                if(row[value] == 2):
                    row[value]=row[value]+1
            field.insert(0, row)#Insert next row at the top of the screen
        else:#If the character has moved backwards and is lagging behind
            buffer = buffer + 1
            player_x -= 1
        field[player_x][player_y]=2
 
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        field[player_x][player_y]=0
        if(player_x < x_field - 1):
            player_x += 1
        buffer = buffer - 1#Detect whether the player is lagging behind by moving backwards
        field[player_x][player_y]=2
        
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        field[player_x][player_y]=0
        if(player_y > 0):
            player_y -= 1
        field[player_x][player_y]=2
 
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        field[player_x][player_y]=0
        if(player_y < y_field - 1):
            player_y += 1
        field[player_x][player_y]=2

def main():
    # Setup player
    global player_x, player_y
    player_x = x_field // 2
    player_y = y_field // 2
 
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
                tcod.console_put_char(0, y, x, field[x][y], tcod.BKGND_NONE)
        #tcod.console_put_char(0, player_x, player_y, '@', tcod.BKGND_NONE)
        tcod.console_flush()
        #tcod.console_put_char(0, player_x, player_y, ' ', tcod.BKGND_NONE)
        for y in range(y_field):
            for x in range(x_field):
                tcod.console_put_char(0, x, y, field[x][y], tcod.BKGND_NONE)
        str_x=str(player_x)
        str_y=str(player_y)
        conn.execute("INSERT INTO PLAYERONE (ID,X,Y,HEALTH) \
      VALUES (20, "+str_x+", "+str_y+", 40 )")
 
        exit_game = handle_keys()
 
 
main()
