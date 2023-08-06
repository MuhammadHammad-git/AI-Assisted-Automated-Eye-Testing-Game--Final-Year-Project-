import pygame
pygame.font.init()
Optotype_Letter_sizes = [368, 243, 243, 190, 190, 190, 190, 130, 130, 130, 130, 130, 89, 89, 89, 89, 89, 89,
                         53, 53, 53, 53, 53, 53, 53, 38, 38, 38, 38, 38, 38, 38, 38]
optotye_list_size = len(Optotype_Letter_sizes)
optotypes = []
for i in range(optotye_list_size):
    optotypes.append(pygame.font.Font("MAIN_Proj/Optician-Sans.otf", int(Optotype_Letter_sizes[i])))


# Optotype displayer function
def display(screen, size_no, letter, position, color):
    text = optotypes[size_no].render(letter, True, color)
    text_rect = text.get_rect(center = (position[0], position[1]))
    # Calculate the position of the frame
    # Blit the frame and the text onto the screen
    screen.blit(text, text_rect)
    pygame.display.update()
