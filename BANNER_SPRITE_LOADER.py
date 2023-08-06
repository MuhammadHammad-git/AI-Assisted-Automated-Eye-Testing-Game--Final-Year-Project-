import pygame
import spritesheet


def banner_animation(color):
    Wood_Banner_Sprite = pygame.image.load('Spritesheets/Custom/PosterSprite.png').convert_alpha()
    Banner_Frame = spritesheet.SpriteSheet(Wood_Banner_Sprite)

    ini_width, ini_height = 391, 417
    animations = [[]]
#                 [368, 243, 243, 190, 190, 190, 190, 130, 130, 130, 130, 130, 89,    89, 89, 89, 89, 89, 53, 53, 53, 53, 53, 53, 53, 38, 38, 38, 38, 38, 38, 38, 38]
    scale_arr = [0.55, 0.48, 0.48, 0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]
    for F in range(0, len(scale_arr), 1):
        if F != 0:
            animations.append([])
        start_x, start_y = 0, 0
        for L in range(19, 0, -1):
            animations[F].append(
                Banner_Frame.get_image(startx=start_x, starty=start_y, width=ini_width, height=ini_height, scale=scale_arr[F],
                                       color=color, banner_mod=True))
            start_x += ini_width
    print(len(animations))
    print(len(animations[1]))
    return animations
