from random import randint
field= []
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))
mines = int(input("Please enter the number of mines: "))
for x in range(rows):
    field.append([])
    for y in range(columns):
        field[x].append(0)
for x in range(mines):
    mine = False
    while(mine == False):
        r = randint(0, rows - 1)
        c = randint(0, columns - 1)
        if(field[r][c] ==0):
            field[r][c] = field[r][c] + 1
            mine = True
for x in range(rows):
    print(field[x])
play_field=[]
for x in range(rows):
    play_field.append([])
    for y in range(columns):
        play_field[x].append(0)
win=False
while(win == False):
    for x in range(rows):
        print(play_field[x])
    playx=int(input("Row: "))
    playy=int(input("Column: "))
    if(field[playx][playy] == 1):
        print("DEATH")
        win = True
    try:
        if(field[playx + 1][playy] == 1):
            play_field[playx][playy]=play_field[playx][playy] + 1
    except:
        play_field[playx][playy]=play_field[playx][playy]
    try:
        if(field[playx + 1][playy + 1] == 1):
            play_field[playx][playy]=play_field[playx][playy] + 1
    except:
        play_field[playx][playy]=play_field[playx][playy]
    try:
        if(field[playx][playy + 1] == 1):
            play_field[playx][playy]=play_field[playx][playy] + 1
    except:
        play_field[playx][playy]=play_field[playx][playy]
    try:
        if(field[playx - 1][playy + 1] == 1):
            play_field[playx][playy]=play_field[playx][playy] + 1
    except:
        play_field[playx][playy]=play_field[playx][playy]
    try:
        if(field[playx - 1][playy] == 1):
            play_field[playx][playy]=play_field[playx][playy] + 1
    except:
        play_field[playx][playy]=play_field[playx][playy]
    try:
        if(field[playx - 1][playy - 1] == 1):
            play_field[playx][playy]=play_field[playx][playy] + 1
    except:
        play_field[playx][playy]=play_field[playx][playy]
    try:
        if(field[playx][playy - 1] == 1):
            play_field[playx][playy]=play_field[playx][playy] + 1
    except:
        play_field[playx][playy]=play_field[playx][playy]
    try:
        if(field[playx + 1][playy - 1] == 1):
            play_field[playx][playy]=play_field[playx][playy] + 1
    except:
        play_field[playx][playy]=play_field[playx][playy]
