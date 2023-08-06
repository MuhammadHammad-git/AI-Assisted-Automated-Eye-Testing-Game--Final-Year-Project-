# IMPORTS
import My_colors as color
from instructions import placehand as ins
import random
import threading
import queue as q
import pygame
import button
import Optotype_Displayer
import BANNER_SPRITE_LOADER as BA
import My_colors
import spritesheet
from MAIN_Proj import MA
from MAIN_Proj import Slidingwind as sliding
import Default_screen_res as sr

# Imports end
pygame.init()

s_w, s_h = sr.screen_width_def, sr.screen_height_def
screen = pygame.display.set_mode((s_w, s_h))
pygame.display.set_caption("MAIN GAME")

banner_anim = BA.banner_animation(color.Black)
no_frame = 32

# background_img = pygame.image.load('Spritesheets/game_background/game_background_4/game_background_4.png')
background_img = pygame.transform.smoothscale((pygame.image.load('Spritesheets/game_background/game_background_4/game_background_4.png')), (pygame.display.Info().current_w, pygame.display.Info().current_h))

result_pad = pygame.transform.smoothscale((pygame.image.load('Result_screen/Resultpad/Resultpad1.png')),
                                             (s_w, s_h))


Letters = ["F", "L", "O", "T", "Z"]

F_loc = []
thcolor = color.Black
frame_len = 50
for i in range(frame_len):
    F_loc.append((random.randint(0, 1200), random.randint(200, s_h-210)))

pause = False
j = 18
up = False
run = True
size = 0
banner_loc = [s_w/2, s_h/2]

letter_num = 0
result = True
the_end = False
# Define a function that inverts a boolean and returns a letter

def invert_bool_and_return_a(eventf):
    global queue, pause, j, up, run, banner_loc, letter_num, thcolor, size, result, the_end
    missed = 0
    userin_letter = "Background_noise"
    guess = True
    sliding.audio_ini()
    while run:
        eventf.wait()
        if up:
            j += 1
            if j == 18:

                banner_loc = [random.randint(100, s_w - 100), random.randint(250, s_h-250)]
                size += 1
                if size == no_frame:
                    # initialize the game
                    result = False
                    the_end = True
                    pygame.time.delay(100)
                    ####
                    pause = False
                    j = no_frame
                    up = False
                    run = False
                    #size = 1
                    banner_loc = [s_w / 2, s_h / 2]
                    letter_num = 0
                    ####

                    #run = False
                up = False
        else:
            j -= 1
            if j == 0:

                pause = True
                letter_num = random.randint(0, 4)
                while userin_letter == "Background_noise" and run:
                    print("-------", guess, "---------------")
                    print("-----------------------------------------------------")
                    userin_letter = MA.machine_learning_model(First_time=guess)
                    print("-----------------------------------------------------")
                    guess = False
                    if userin_letter != "Background_noise":
                        if userin_letter == Letters[letter_num]:
                            thcolor = color.Green
                            pygame.time.delay(100)
                            thcolor = color.Black
                            guess = True
                        else:
                            missed += 1
                            j-=1
                            thcolor = color.Red
                            pygame.time.delay(100)
                            thcolor = color.Black
                    if missed > 2:
                        run = False
                        result = False

                userin_letter = "Background_noise"
                guess = True
                print("-----------------------------------------------------")
                print(userin_letter, "-------", Letters[letter_num])
                print("-----------------------------------------------------")
                pygame.time.delay(100)
                pause = False
                up = True
        # Clear the event
        eventf.clear()


# Create an event to signal the background thread
eve = threading.Event()

# Create a queue to communicate between the threads
queue = q.Queue()

# Start the background thread
t = threading.Thread(target=invert_bool_and_return_a, args=(eve,))


def background(button_sprite):
    # Initialize the boolean value to True
    global j, run, banner_loc, letter_num, thcolor, result, the_end, size

    #
    #
    exit_btn = button.Button(s_w - 120, 0, button_sprite, elevation=20)
    clock = pygame.time.Clock()

    sprite_sheet_image = pygame.image.load('Spritesheets/grasstrans.png').convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
    t.start()

    grass_colour = My_colors.Black
    # get_image(self, startx, starty, width, height, scale, colour):
    animations = [sprite_sheet.get_image(startx=650, starty=630, width=700, height=900, scale=0.1,
                                         color=grass_colour),
                  sprite_sheet.get_image(startx=1400, starty=630, width=700, height=900, scale=0.1,
                                         color=grass_colour),
                  sprite_sheet.get_image(startx=2200, starty=630, width=700, height=900, scale=0.1,
                                         color=grass_colour),
                  sprite_sheet.get_image(startx=3000, starty=630, width=700, height=900, scale=0.1,
                                         color=grass_colour)]

    bottom_grass = sprite_sheet.get_image(startx=500, starty=4250, width=6550, height=780, scale=0.2,
                                          color=grass_colour, scaling=True, banner=True)
    frame = 0
    pos = (0, 0)
    show_ins = True
    increm = 0
    frame = 0

    while run:

        if result:
            if show_ins:
                ins.ins(1)
                pygame.time.delay(3000)
                show_ins = False
            screen.blit(background_img, (0, 0))
            if exit_btn.draw(screen, pos):
                run = False
                eve.set()
                break
            screen.blit(bottom_grass, (s_w - (bottom_grass.get_width()), s_h - (s_h * 0.2)))
            screen.blit(bottom_grass, (s_w - (bottom_grass.get_width()), s_h - (s_h * 0.15)))

            for fi in range(frame_len):
                screen.blit(animations[frame],
                            F_loc[fi])  # Blit the current frame of the animation to the screen at its position

            eve.set()
            if frame < (len(animations) - 1):
                increm += 1
                if increm % 5 == 0:
                    frame += 1
                if increm == 100:
                    increm = 0
            else:
                frame = 0

            banner_rect = banner_anim[size][j].get_rect(center = banner_loc)
            # Update the frame index for each animation
            screen.blit(banner_anim[size][j], banner_rect)
            if pause:
                Optotype_Displayer.display(screen=screen, size_no=size, letter=Letters[letter_num], position=banner_loc,
                                           color=thcolor)
            pygame.display.update()

        # get mouse position
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
        clock.tick(60)
    t.join()
    # pygame.font.quit()
    print("Exited")
    size-=1
    return size, screen, the_end, result_pad, background_img
