import pygame
import My_colors as color
# import screen_initializer as si
# pygame.init()
# screen = si.ini_screen()

import BANNER_SPRITE_LOADER as BA
animations = BA.banner_animation(color.White)


def animate(screen, Direction, banner_loc, speed=100):
    Total_animation_frames = len(animations)
    if Direction:
        step = [Total_animation_frames]
    else:
        step = [Total_animation_frames, -1, -1]
    for animation in range(*step):
        screen.fill(color.White)
        # Update the frame index for each animation
        screen.blit(animations[animation],
                    banner_loc)  # Blit the current frame of the animation to the screen at its position
        pygame.time.delay(speed)
        pygame.display.update()

#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#     animate(screen, True, (100, 100), speed=250)
