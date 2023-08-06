import os
import pygame
import Default_screen_res as defsr
import My_colors
import button
import spritesheet
import My_colors as color
script_path = os.path.dirname(os.path.abspath(__file__))+"/"

message_map = {
   368: ("YOU ARE BLIND!", "Contact you doctor!"),
   243: ("6/60", "5-6.75", "Severe Vision Loss"),
   190: ("6/36", "2.25-5", "Moderate Vision"),
   130: ("6/24", "1.25-3.75" ,"Moderate Vision"),
   89: ("6/18", "1-2.5", "Mild Vision"),
   53: ("6/12", "0.75-1.75", "Mild Vision "),
   38: ("6/9", "0.5-1.5", "Normal Vision"),
    0: ("6/6", "0-1.0", "Normal Vision")
}

letters = ["F", "L", "O", "T", "Z"]
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
mistake = 0
font2 = [368, 243, 243, 190, 190, 190, 190, 130, 130, 130, 130, 130, 89, 89, 89, 89, 89, 89, 53, 53, 53, 53, 53, 53,
         53, 38, 38, 38, 38, 38, 38, 38, 38]
# Text_font = pygame.font.SysFont(name=None, size=36)
Text_font = pygame.font.Font(script_path+'T.ttf', 30)
Status = False
def text_display_func(screen, rtext1, rtext2, rtext3, index):
    global y, X, Y, Text_font
    y = 25
    w = screen.get_width()/2
    h = screen.get_height()/2
    surf = pygame.Surface((400,200))
    surf.fill((254,254,254))
    rect = surf.get_rect(center = (w, h))
    screen.blit(surf, rect)
    fmf = Text_font.render(rtext1, True, My_colors.BROWN)
    text_pos = (w-220, h+10)
    screen.blit(fmf, text_pos)
    text_pos = (w-250, h+60)
    fmf1 = Text_font.render(rtext2, True, My_colors.BROWN)
    screen.blit(fmf1, text_pos)
    fmf2 = Text_font.render(rtext3, True, My_colors.BROWN)
    text_pos = (w - 100, h - 20)
    screen.blit(fmf2, text_pos)
    pygame.display.update()

def overlay(screen, back):
    screen.blit(back, (0, 0))
    overlay = pygame.Surface((screen.get_width(), screen.get_height()))
    overlay.set_alpha(160)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))



def pad_animation(screen, resultcard, back):
    for i in range(700, 100, -40):
        overlay(screen, back)
        screen.blit(resultcard, (0,i))
        pygame.display.update()
    for i in range(100, 10, -4):
        overlay(screen, back)
        screen.blit(resultcard, (0,i))
        pygame.display.update()
    for i in range(10, 0, -1):
        overlay(screen, back)
        screen.blit(resultcard, (0,i))
        pygame.display.update()
    pass


def disp_result(m_screen, i, back = None, pad=None, button_sprite=None, mistakes = 1, theend = True):
    s_w = m_screen.get_width()
    wood_button_sprite = pygame.image.load('Spritesheets/wood button interface/wood_buttons_trans.png').convert_alpha()
    wood_button = spritesheet.SpriteSheet(wood_button_sprite)
    wood_button_exit = wood_button.get_image(startx=1150, starty=200, width=900, height=900, scale=0.1, banner=True)
    exit_b = button.Button((s_w - wood_button_exit.get_width()), 0, wood_button_exit, elevation=20)
    overlay(m_screen, back)
    pygame.display.update()
    m_screen.fill((255,255,255))
    global font2, mistake, message_map
    results_shown = False
    run = True
    pos = (0,0)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
        if exit_b.draw(m_screen, pos):
            print("here")
            run = False
        if not results_shown:
            pad_animation(m_screen, pad, back)
            results_shown = True
        if theend:
            text_display_func(m_screen, f"    VISUAL ACUITY IS : {message_map[0][0]}",
                              f"   ESTIMATED RANGE IS  : {message_map[0][1]}", message_map[0][2], 18)
        else:
             text_display_func(m_screen, f"   VISUAL ACUITY IS : {message_map[font2[i]][0]}",
                               f"   ESTIMATED RANGE IS  : {message_map[font2[i]][1]}", message_map[font2[i]][2], 18)

    return Status