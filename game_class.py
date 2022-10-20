import pygame

class Game:
    # initialize game
    def __init__(self):
        pygame.init()

    def game_window(self, x, y):
        return pygame.display.set_mode((x, y))

    def game_title(self, x):
        return pygame.display.set_caption(x)

    def game_image(self, img):
        return pygame.image.load(img)

    def game_icon(self, img):
        return pygame.display.set_icon(img)

    def color_fill(self,screen,R,G,B):
        return screen.fill((R,G,B))

    def draw_over_screen(self,screen,img,x_axis,y_axis):
        return screen.blit(img, (x_axis, y_axis))

    def game_screen_update(self):
        return pygame.display.update()


