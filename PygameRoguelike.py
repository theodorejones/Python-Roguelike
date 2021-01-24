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
    for y in range(y_field):
        field.append(0)
#ID, health, and attack, in that order, per square

def swap(field, pos1, pos2):
    print(field)
    field[pos1],field[pos2]=field[pos2],field[pos1]
    print(field)
    return field

def game_loop():
    global field
    x=1
    y=1
    print(x)
    print(y)
    pos=y*x_field+x
    field[pos]=1
    print(pos)
    print(field)

    gameExit = False
    pressed = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            try:
                if event.type == pygame.KEYDOWN and pressed == False:
                    if event.key == pygame.K_LEFT:
                        field=swap(field,pos,pos-1)
                        x=x-1
                        print(x)
                        print(y)
                        pos=(y*x_field-1)+x
                        print(pos)
                        print(field)
                    if event.key == pygame.K_RIGHT:
                        field=swap(field,pos,pos+1)
                        x=x+1
                        print(x)
                        print(y)
                        pos=(y*x_field-1)+x
                        print(pos)
                        print(field)
                    if event.key == pygame.K_UP:
                        field=swap(field,pos,pos-x_field)
                        y=y-1
                        print(x)
                        print(y)
                        pos=(y*x_field-1)+x
                        print(pos)
                        print(field)
                    if event.key == pygame.K_DOWN:
                        field=swap(field,pos,pos+x_field)
                        y=y+1
                        print(x)
                        print(y)
                        pos=(y*x_field-1)+x
                        print(pos)
                        print(field)
                    pressed = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        pressed = False
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        pressed = False
            except:
                print("Boundary")
        gameDisplay.fill(white)
        for x in range(x_field):
            for y in range(y_field):
                pos=(y*x_field-1)+x
                if(field[pos] == 1):
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
