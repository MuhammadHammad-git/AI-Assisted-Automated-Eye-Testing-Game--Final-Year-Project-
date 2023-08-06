import pygame


# button class
class Button:
    def __init__(self, x, y, image, elevation=15):
        self.elevation = elevation
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = image
        self.image_org = image
        self.rect_org = self.image.get_rect(topleft = (x, y))
        self.x = x
        self.y = y
        self.clicked = False
        self.changed = False
        self.image2 = pygame.transform.smoothscale(image, (self.width * 0.85, self.height * 0.85))

    def draw(self, surface, pos):
        action = False
        ychange = self.y-(self.height*0.05)
        xchange = self.x-(self.width*0.05)
        yorg = self.y
        # check mouseover and clicked conditions
        if self.rect_org.collidepoint(pos):
            self.image = self.image_org
            if not self.changed:
                self.y = ychange
                self.x = xchange
                self.changed = True
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.y = ychange + self.elevation
            else:
                if self.clicked:
                    # pygame.time.delay(100)
                    action = True
                    self.clicked = False
        else:
            self.image = self.image2
            if self.changed:
                self.y = self.rect_org.y
                self.x = self.rect_org.x
                self.changed = False

        # print(self.changed)
        # draw button on screen
        surface.blit(self.image, (self.x, self.y))
        return action

    def pressed(self, surface):
        surface.blit(self.image, (self.rect_org.x, self.rect_org.y))
        pygame.time.delay(1000)
