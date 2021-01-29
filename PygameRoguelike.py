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

field=[]
for x in range(x_field):
    field.append(0)
field[3]=1

start = True
def swap(field, pos1, pos2):
    field[pos1],field[pos2]=field[pos2],field[pos1]
    return field

def game_loop():
    global field
    global start
    gameExit = False
    pressed = False

    while not gameExit:
        if(start == True):
            for x in range(x_field):
                if(field[x] == 1):
                    print("Player")
                else:
                    print("Generating...")
                    field[x] = randint(2,6)
                    print(field[x])
            start = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            try:
                if event.type == pygame.KEYDOWN and pressed == False:
                    if event.key == pygame.K_LEFT:
                        print("Left")
                    if event.key == pygame.K_RIGHT:
                        print("Right")
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
