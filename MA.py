import pygame


def machine_learning_model(i, Bool=False):
    Letters = ["F", "L", "O", "T", "Z"]
    print("asking", Letters[i])
    pygame.time.delay(2000)
    print("Replying", Letters[i])
    return Letters[i]
