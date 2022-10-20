import pygame
from game_class import Game


def draw_in_screen( img, x, y):
    return screen.blit(img, (x, y))

#start your game
game=Game()

# create the screen with height and width
screen=game.game_window(800,600)

# Caption and Icon
game.game_title("My Game")
icon=game.game_image('joystick.png')
game.game_icon(icon)

playerImg=game.game_image("running.png")

def player(x, y):
    draw_in_screen(playerImg, x, y)
playerX=2
playerY=420
playerY_change=0
playerX_change=0
# Background
background = game.game_image('game_bg.png')
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key in (pygame.K_DOWN,pygame.K_UP):
                playerX_change = 0
                playerY_change =0
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY<=0:
        playerY = 0
    elif playerY>=420:
        playerY = 420
    player(playerX, playerY)
    #player(10, 380)

    pygame.display.update()