##package import
import pygame
from game_class import Game
import math
import random

import pygame
from pygame import mixer

#step:1 initiating game
mario_game=Game()

#step:2 screen creation
window_x_axis=800
window_y_axis=600
game_screen =mario_game.game_window(window_x_axis, window_y_axis)
width = game_screen.get_width()
height = game_screen.get_height()
background=mario_game.game_image("game_bg.png")

#step:3 Caption and Icon
mario_game.game_title("My Game")
title_icon=mario_game.game_image('joystick.png')
mario_game.game_icon(title_icon)

#Step:4 Sound
mixer.music.load("mario_bg.mp3")
mixer.music.play(-1)

#Step:5 Player Setup
playerImg=mario_game.game_image("spaceship.png")
playerX=370
playerY=480
playerX_change = 0

#Step:6 Enemy Setup
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(mario_game.game_image('monster.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.1)
    enemyY_change.append(10)

#Step:7 Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = mario_game.game_image('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#Step:8 Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

#Step:9 Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


def player(x, y):
    game_screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    game_screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    game_screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, green,blue)
    game_screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    game_screen.blit(over_text, (200, 250))

# Game Starting Loop
running = True
while running:
    # Setting up Background Image
    game_screen.blit(background, (0, 0))

    #Creating action for Buttons
    for event in pygame.event.get():

        #Exit while press cross button making screen to terminate.
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left and giving movement to the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            #if space ar pressed firing the bullet.
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        #if keystroke up then no action.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #player movement constraint not moving outside screen
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over if any enemy reaches the player moving area
        if enemyY[i] > 440:

            ##moving all enemies out of the screen.
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        #moving enemies in x axis based on x_change value.
        enemyX[i] += enemyX_change[i]

        #moving enemy step by step in x axis.
        # if he reaches end of screen stepping down the position in y axis
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # Collision -Hitting the enemy by using bullet using distance formula.
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

        #if collision occurs creating bullet explosion sound and creating one more bullet ready
        #creating one more enemy in random location.
        if collision:
            explosionSound = mixer.Sound("explosion_sound.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()

