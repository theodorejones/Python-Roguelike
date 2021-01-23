import pygame

pygame.init()
x_field = 3
y_field = 3
pixel = 128
display_width = x_field * pixel
display_height = y_field * pixel

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73
car_height = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Will Of The Dungeon')
clock = pygame.time.Clock()

person = pygame.image.load('person.png')
monster = pygame.image.load('monster.png')
sword = pygame.image.load('sword.png')
shield = pygame.image.load('shield.png')
wall = pygame.image.load('wall.png')

def player(x,y):
    gameDisplay.blit(person,(x,y))

field=[]
for x in range(x_field):
    field.append([])
    for y in range(y_field):
        field[x].append([0,0,0])
#ID, health, and attack, in that order, per square
'''When the player moves, the current and destination squares will swap,
and the game will make decisions based on the given statistics. For instance, a
Sword or Shield will raise a character's Attack or Health, respectively, and a
Monster will attack the player as it passes if the player's Attack isn't enough to
kill it'''
def swap(field, x1, y1, x2, y2):
    temp=field[x1][y1]
    field[x1][y1]=field[x2][y2]
    field[x2][y2]=temp
    return field

def game_loop():
    global field
    field[1][1]=[1,0,0]
    x=1
    y=1
    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    field=swap(field,x,y,x-1,y)
                if event.key == pygame.K_RIGHT:
                    field=swap(field,x,y,x+1,y)
                if event.key == pygame.K_UP:
                    field=swap(field,x,y,x,y-1)
                if event.key == pygame.K_DOWN:
                    field=swap(field,x,y,x,y+1)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        for x in range(x_field):
            for y in range(y_field):
                if(field[x][y][0] == 1):
                    print(x)
                    print(y)
                    print(field)
                    gameDisplay.blit(person,(128*x,128*y))

        if x > display_width - car_width or x < 0:
            gameExit = True
        if y > display_height - car_height or y < 0:
            gameExit = True
        
        pygame.display.update()
        clock.tick(10)



game_loop()
pygame.quit()
quit()
quit()
