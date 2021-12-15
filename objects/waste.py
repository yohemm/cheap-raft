import pygame
import random

class Waste:
    def __init__(self):
        self.name = random.choice(list(inventory.keys()))

        self.quantity = random.randint(1, 5)
        self.pos = [-20, random.randint(0, SCREEN_SIZE[1]) - 400]
        self.velocity = random.randint(1, 2)
        self.imageSize = 60

    def __repr__(self):
        return ' name : ' + self.name + 'pos : ' + str(self.pos) + ' quantity : ' + str(self.quantity)

    def blit(self):
        if self.name == 'wood':
            img = pygame.transform.scale(WOOD, (self.imageSize,self.imageSize))
        elif self.name == 'leaf':
            img = pygame.transform.scale(LEAF, (self.imageSize,self.imageSize))
        else:
            img = pygame.transform.scale(PLASTIC, (self.imageSize,self.imageSize))
        self.pos = [self.pos[0] + self.velocity + wavesEffect[0], self.pos[1] + self.velocity + wavesEffect[1]]
        SCREEN.blit(img, self.pos)
    def onClick(self):
            inventory[self.name] += self.quantity