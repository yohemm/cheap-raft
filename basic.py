import pygame
def realPos(position, SCREEN, UNITY):
    return (position[0] * UNITY + (SCREEN.get_size()[0] // 2 - UNITY // 2),
     position[1] * UNITY + (SCREEN.get_size()[1] // 2 - UNITY // 2))

def moussePosMap(SCREEN, UNITY):
    return (pygame.mouse.get_pos()[0] - SCREEN.get_size()[0] // 2 + UNITY // 2)//UNITY,  (pygame.mouse.get_pos()[1] - SCREEN.get_size()[1] // 2 + UNITY // 2)//UNITY

def whatAround(posMap:list, rafts):
    result = []
    for singleRaft in rafts:
        if [singleRaft.position[0] - posMap[0] , singleRaft.position[1] - posMap[1]] in [[1, 0],[-1, 0],[0, 1], [0, -1]] and not singleRaft.position == posMap:
            result.append(singleRaft)
    return result

def mousseOver(entity):
    return entity.position[0] < pygame.mouse.get_pos()[0] < entity.position[0] + entity.size[0] and andentity.position[1] < pygame.mouse.get_pos()[1] < entity.position[1] + entity.size[1]

class Text:
    def __init__(self, text:str, height:int = 25, font:str='Supermercado.ttf', position:list = [0,0], color = (00,00,00)):
        self.position = position
        self.font = font
        self.text = text
        self.color = color
        self.fontHeight = height
        self.font = pygame.font.Font('src/'+self.font, self.fontHeight)
        self.changeText(self.text)


        self.size = [0,0]
        for render in self.renders:
            if self.size[0] < render.get_size()[0]:
                self.size = [render.get_size()[0], self.size[1]]
            self.size = [self.size[0], self.size[1] + render.get_size()[1]]

    def changeText(self, newText:str):
        self.text = newText
        self.renders = []
        for line in self.text.splitlines():
            self.renders.append(self.font.render(line, True, self.color))
        self.size = [0,0]
        for render in self.renders:
            if self.size[0] < render.get_size()[0]:
                self.size = [render.get_size()[0], self.size[1]]
            self.size = [self.size[0], self.size[1] + render.get_size()[1]]
    def changeColor(self, newColor:tuple):
        self.color = newColor
        for line in self.text.splitlines():
            self.renders.append(self.font.render(line, True, self.color))



    def blit(self, SCREEN, alignX:str=None):
        positionlines = self.position
        for idLine in range(len(self.renders)):
            if alignX == 'right':
                positionlines = [SCREEN.get_size()[0] - self.renders[idLine].get_size()[0], positionlines[1]]
            elif alignX == 'center':
                positionlines = [SCREEN.get_size()[0]//2 - self.renders[idLine].get_size()[0]//2, positionlines[1]]
            SCREEN.blit(self.renders[idLine], positionlines)
            positionlines = [positionlines[0], positionlines[1] + self.renders[idLine].get_size()[1]]

class TextButton:
    def __init__(self, text:Text, ):
        self.text = text

    def click(self):
        return self.text.position[0] < pygame.mouse.get_pos()[0] < self.text.position[0] + self.text.size[0] and self.text.position[0] < pygame.mouse.get_pos()[0] < self.text.position[0] + self.text.size[0] and pygame.mouse.get_pressed()[0]
    def blit(self, screen):
        self.text.blit(screen)

class ImageButton:
    def __init__(self, pos, size, image, selected):
        self.selected = selected
        self.image = image
        self.pos = pos
        self.size = size

    def click(self):
        if pygame.mouse.get_pressed()[0] and mousseOver(self):self.selected = not self.selected

class Menu:
    def __init__(self, pos:list = [0,0], size:list = [50,50], btnImgs:list = [], texts:list = []):
        self.scroll = 0
        self.position = pos
        self.size = size
        self.images = btnImgs
        self.texts = texts

    def scroll(self):
        pass

