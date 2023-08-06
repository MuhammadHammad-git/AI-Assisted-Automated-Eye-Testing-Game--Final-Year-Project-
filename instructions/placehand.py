import pygame
import Default_screen_res as sr
import My_colors as C
def ins(status):
    pygame.init()
    s_w = sr.screen_width_def
    s_h = sr.screen_height_def
    screen = pygame.display.set_mode((s_w, s_h))
    pygame.display.set_caption("InstructionScreen")
    if status != 1:
        pygame.quit()
        return status
    scale = 0.5
    placehand = pygame.image.load(
        "C:/Users/Muhammad Hammad Khan/PycharmProjects/pythonProject1/Spritesheets/instructions/placehand.png")
    image = pygame.transform.scale(placehand, (
        s_w * scale, s_h * (scale+0.3)))
    image.set_colorkey(C.Black)

    font = pygame.font.SysFont('timesnewroman', 30)
    text = "PLACE YOURPALM ON ONE EYE"
    text_surface = font.render(text, False, (0, 0, 0))
    rect = text_surface.get_rect()
    rect.center = (s_w*0.5, s_h-100)  # Position the text at the bottom of the screen

    screen.fill(C.White)
    screen.blit(text_surface, rect)
    screen.blit(image, (s_w*0.25, 0))
    run  = 1
    while run:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        run = 0