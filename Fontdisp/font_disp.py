import os
import pygame
from pygame.locals import *
import My_colors as color
script_path = os.path.dirname(os.path.abspath(__file__))+"/"
# Define colors
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Custom Font Display')

# Load the custom font
custom_font = pygame.font.Font(script_path+'fonts/T.ttf', 48)
print(script_path)
# Render the text using the custom font
text = custom_font.render('1234/', True, BROWN)

# Get the rectangle of the text
text_rect = text.get_rect()
text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the screen with a white background
    screen.fill(WHITE)

    # Draw the text on the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
