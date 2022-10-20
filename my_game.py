##package import
import pygame
from game_class import Game

#step:1 initiating game
mario_game=Game()


#step:2 screen creation
window_x_axis=800
window_y_axis=600
game_screen =mario_game.game_window(window_x_axis, window_y_axis)

#step:3 Caption and Icon
mario_game.game_title("My Game")
title_icon=mario_game.game_image('joystick.png')
mario_game.game_icon(title_icon)

def game_screen_action(game_screen,running=True):
    while running:

        # image upload ->Background Image
        background=mario_game.game_image("game_bg.png")
        #drawing ->  over the game screen
        mario_game.draw_over_screen(game_screen,background,0,0)

        running=game_button_actions()
        #update the game screen with above changes
        mario_game.game_screen_update()

def game_button_actions():

    #exit functionality from button events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return  False
    return True

game_screen_action(game_screen)