import pygame
from random import randint
pygame.init()
x_field = 7
y_field = 1
pixel = 128
display_width = 7 * pixel
display_height = 3 * pixel

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Will Of The Dungeon')
clock = pygame.time.Clock()

captain = pygame.image.load('captain.png')
person = pygame.image.load('person.png')
ship = pygame.image.load('ship.png')
cannon = pygame.image.load('cannon.png')
chest = pygame.image.load('chest.png')
wheel = pygame.image.load('wheel.png')
def player(x,y):
    gameDisplay.blit(person,(x,y))
stats = [10,10,10,10]
#Reputation, Resources, Ship Health, Crew Health
def score(stats, field, state):
    if(state == "l"):
        fore, aft = field[2],field[4]
    else:
        fore, aft = field[4],field[2]
    #Add or subtract stats based on input
    #2: Person
    #3: Ship
    #4: Cannon
    #5: Chest
    #6: Wheel
    if(fore == 2):
        stats[3] += 1
        stats[1] -=1
    if(fore == 3):
        stats[3] += 1
        stats[1] -=1
    if(fore == 4):
        stats[3] += 1
        stats[1] -=1
    if(fore == 5):
        stats[3] += 1
        stats[1] -=1
    if(fore == 6):
        stats[3] += 1
        stats[1] -=1
field=[]
for x in range(x_field):
    field.append(0)
field[3]=1

start = True
def swap(field, pos1, pos2):
    field[pos1],field[pos2]=field[pos2],field[pos1]
    return field
def move_left(field):
    field[3 - 1]=0
    for x in range(2,0,-1):
        if(field[x]<field[x-1]):
            swap(field,x,x-1)
    field[0]=randint(2,6)
def move_right(field):
    field[3 + 1] = 0
    for x in range(4,6,1):
        if(field[x]<field[x+1]):
            swap(field,x,x+1)
    field[6]=randint(2,6)
def game_loop():
    global field
    global start
    global stats
    gameExit = False
    pressed = False

    while not gameExit:
        if(start == True):
            for x in range(x_field):
                if(field[x] == 1):
                    print("Generating...")
                else:
                    field[x] = randint(2,6)
            start = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            try:
                if event.type == pygame.KEYDOWN and pressed == False:
                    if event.key == pygame.K_LEFT:
                        move_left(field)
                        stats=score(stats, field, "l")
                    if event.key == pygame.K_RIGHT:
                        move_right(field)
                        stats=score(stats, field, "r")
                    pressed = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        pressed = False
            except:
                print("Boundary")
        gameDisplay.fill(white)
        mark = 0
        for x in range(len(field)):
            mark = field[x]
            if(mark == 1):
                gameDisplay.blit(captain,(128*x,128))
            elif(mark == 2):
                gameDisplay.blit(person,(128*x,128))
            elif(mark == 3):
                gameDisplay.blit(ship,(128*x,128))
            elif(mark == 4):
                gameDisplay.blit(cannon,(128*x,128))
            elif(mark == 5):
                gameDisplay.blit(chest,(128*x,128))
            elif(mark == 6):
                gameDisplay.blit(wheel,(128*x,128))
        
        pygame.display.flip()
        clock.tick(10)



game_loop()
pygame.quit()
quit()
quit()
