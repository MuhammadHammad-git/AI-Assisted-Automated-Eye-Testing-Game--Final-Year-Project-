import pygame
import button
import spritesheet
import threading
from MAIN_Proj import Slidingwind as sliding
from Mainmenueuser import userinput
import queue as que
import Default_screen_res as sr
import My_colors as Cs
from pygame import FULLSCREEN
thstart = False
guess = True
run = True
thstop= 1
def ML(eventf):
    global thstart, thstop, guess, run
    user = "Background_noise"
    sliding.audio_ini()
    while run:
        eventf.wait()
        while user == "Background_noise" and run:
            ans = userinput.answer(First_time=guess)
            guess = False
            if ans != "Background Noise":
                if ans == "Yes":
                    thstart = True
                    guess = True
                    thstop = 1
                    run = False
                elif ans == "No":
                    thstop = 0
                    run = False

        # Clear the event
        eventf.clear()
# Create an event to signal the background thread
ML_event = threading.Event()

# Create a queue to communicate between the threads
queue = que.Queue()

# Start the background thread
th = threading.Thread(target=ML, args=(ML_event,))

def main_menu(status):
    global run, thstop
    th.start()
    ML_event.set()
    pygame.init()
    s_w = sr.screen_width_def
    s_h = sr.screen_height_def
    screen = pygame.display.set_mode((s_w, s_h))
    pygame.display.set_caption("Main Menu")
    if status != 1:
        pygame.quit()
        return status
    # create display window
    # load button images

    wood_button_sprite = pygame.image.load('Spritesheets/wood button interface/wood_buttons_trans.png').convert_alpha()
    wood_button = spritesheet.SpriteSheet(wood_button_sprite)
    wood_button_start = pygame.image.load('start_btnComp.png').convert_alpha() #  = wood_button.get_image(startx=250, starty=200, width=900, height=900, scale=0.2)
    wood_button_exit = wood_button.get_image(startx=1150, starty=200, width=900, height=900, scale=0.1, banner=True)
    wood_button_exit2 = wood_button.get_image(startx=1150, starty=200, width=900, height=900, scale=0.1, banner=True)
    Wood_Banner = pygame.image.load('Spritesheets/wooden sign banner/Wood_banner_trans.png').convert_alpha()
    wood_banner = pygame.transform.smoothscale(Wood_Banner, (s_w / 1.5, s_h / 2))

    Sky_Back = pygame.image.load('Spritesheets/sky_Background/sky.jpg').convert_alpha()
    sky_back = pygame.transform.smoothscale(Sky_Back, screen.get_size())
    inscloud = pygame.image.load('Spritesheets/Custom/insCloud1.png').convert_alpha()
    inscloud.set_colorkey((0,0,0))
    # create button instances
    start_btn = button.Button(((s_w-wood_button_start.get_width()) / 2), (s_h / 2)-wood_button_start.get_height(), wood_button_start)
    exit_button = button.Button(s_w - (wood_button_exit.get_width()), 0, wood_button_exit, elevation=20)
    # game loop
    mospos = (0, 0)
    while run:
        screen.blit(sky_back, (0, 0))
        ML_event.set()

        if start_btn.draw(screen, pos=mospos) or thstart:
            print('START')
            status = 1
            run = False
        if exit_button.draw(screen, pos=mospos):
            status = 0
            thstop = 0
            run = False
            print('EXIT')
        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
                ML_event.set()
            if event.type == pygame.MOUSEMOTION:
                mospos = event.pos
        screen.blit(wood_banner, (s_w / 5.7, s_h / 2))
        screen.blit(inscloud, (start_btn.rect_org.topleft[0]+170,start_btn.rect_org.topleft[1]-190))
        pygame.display.update()

    status = thstop
    th.join()

    return status, wood_button_exit, wood_button_exit2
