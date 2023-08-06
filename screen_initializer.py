import pygame


def ini_screen(screen_width=1000, screen_height=500, title='Default_Screen'):
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(title)
    return screen

