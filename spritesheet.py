import pygame


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, startx, starty, width, height, scale=1, color=(0, 0, 0), scaling=True, grass=False, banner=False, banner_mod=False):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), (startx, starty, width, height))
        if scaling:
            if banner:
                image = pygame.transform.smoothscale(image, (
                    image.get_width() * scale, image.get_height() * scale))
                image.set_colorkey(color)
            else:
                if grass:
                    image = pygame.transform.smoothscale(image, (
                        pygame.display.Info().current_w + 400 * scale, pygame.display.Info().current_h - 700 * scale))
                    image.set_colorkey(color)
                if banner_mod:
                    image = pygame.transform.smoothscale(image, (
                        pygame.display.Info().current_w * scale, pygame.display.Info().current_h * (scale+0.3)))
                    image.set_colorkey(color)
                else:
                    image = pygame.transform.smoothscale(image, (
                        pygame.display.Info().current_w * scale, pygame.display.Info().current_h * scale))
                    image.set_colorkey(color)
        return image
