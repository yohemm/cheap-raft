import pygame

types = {
    # Name : imgs, factor
    'fishing': [pygame.transform.scale(pygame.image.load('src/fishing.png'), (100, 100))],
    'watter harvester': [pygame.transform.scale(pygame.image.load('src/watter_harvester.png'), (100, 100))],
    'campfire': [pygame.transform.scale(pygame.image.load('src/campfire.png'), (100, 100))],
    'dormitory': [pygame.transform.scale(pygame.image.load('src/dormitory.png'), (100, 100))],
}
class Build:
    def __init__(self, type:str, level:int = 0):
        self.type = type
        self.level = level
    def __repr__(self):
        return str(self.types) + ' lv' + str(self.level)
    def setImage(self):
        return types[self.type][self.level]
