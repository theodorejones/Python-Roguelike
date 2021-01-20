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
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('person.png')

def player(x,y):
    gameDisplay.blit(carImg,(x,y))
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


def game_loop():
    x = (2*pixel)
    y = (2*pixel)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -pixel
                if event.key == pygame.K_RIGHT:
                    x_change = pixel
                if event.key == pygame.K_UP:
                    y_change = -pixel
                if event.key == pygame.K_DOWN:
                    y_change = pixel

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        player(x,y)

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
