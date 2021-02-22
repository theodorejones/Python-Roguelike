import pygame
from random import randint
pygame.init()
x_field = 200
y_field = 1
pixel = 128
display_width = 3 * pixel
display_height = 3 * pixel

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Heaps Of Treasure')
clock = pygame.time.Clock()

#captain = pygame.image.load('')

def player(x,y):
    gameDisplay.blit(person,(x,y))
stats = [10,10,10]
#Health, Loot, Navigation

field=[]
for x in range(x_field):
    field.append(randint(2,20))

field[0]=1

start = True
def shop(gold):
    level = int(gold/100)
    print("Congratulations on having earned "+str(level) + " cards!")
    return level
def score(stats, item):
    stats[1] = stats[1] + 1
    return stats
def swap(field, pos1, pos2):
    field[pos1],field[pos2]=field[pos2],field[pos1]
    return field

def game_loop():
    global field
    global start
    global stats
    global level
    total_gold = 0
    gameExit = False
    pressed = False

    while not gameExit:
        i = 1
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
                        swap(field, i, 2*i+1)
                        i = 2*i+1
                    if event.key == pygame.K_RIGHT:
                        swap(field, i, 2*i+2)
                        i = 2*i+2
                    pressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        pressed = False
            except:
                print("Boundary")
            if(stats[1] > 10):
                total_gold = total_gold + (stats[1] - 10)
                stats[1] = 10
                print(total_gold)
            print(stats)
            level = shop(total_gold)
        gameDisplay.fill(white)
        mark = 0
        '''for x in range(len(field)):
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
                gameDisplay.blit(wheel,(128*x,128))'''
        
        pygame.display.flip()
        clock.tick(10)



game_loop()
pygame.quit()
quit()
quit()
