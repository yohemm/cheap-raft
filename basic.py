import pygame

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
    def __init__(self, text:str, height:int = 25, position:list = [0,0], font:str='Supermercado.ttf', color = (00,00,00)):
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
    def __init__(self, nameImage:str = 'satisfaction.png', pos = [0,0], size = [100,100], selected:bool = False, ImageButtons:list = []):
        self.selected = selected
        print(nameImage)
        fileName = ''
        for car in nameImage:
            if car == ' ': fileName += '_'
            else : fileName += car

        self.name = ''
        for car in nameImage:
            if car == '.':break
            else:self.name += car
        self.image = pygame.transform.scale(pygame.image.load('src/'+ fileName), size)
        self.pos = pos
        self.size = size
        self.ImageButtons = ImageButtons

    def __repr__(self):
        return self.name+ '     select:' + str(self.selected)+ '     pos:' + str(self.pos)+ '     size:' + str(self.size)

    def click(self):
        if pygame.mouse.get_pressed()[0] and mousseOver(self):self.selected = not self.selected

class Menu:
    def __init__(self, pos:list = [0,0], size:list = [50,50], content:list=[]):
        self.scroll = 0
        self.position = pos
        self.size = size
        self.content = content
        # -1 = aucun
        self.IDselected = -1

    def SelectionSysteme(self):
        if self.position[0] < pygame.mouse.get_pos()[0] < self.position[0] + self.size[0] and self.position[1] < pygame.mouse.get_pos()[1] < self.position[1] + self.size[1]:
            self.IDselected = -1
            print('1')
            for id in range(len(self.content)):
                if self.content[id].click():
                    for cardDiselect in self.content:
                        if not cardDiselect == self.content[id]:
                            cardDiselect.selected = False
                    self.IDselected = id

    def scroll(self):
        pass


class Card:
    def __init__(self, imageBtn:ImageButton, title:Text, cost, selected:bool = False):
        self.imageBtn = imageBtn
        self.title = title
        self.selected = selected
        self.cost = cost
        costStr = ''
        for item in cost:
            costStr += item[0] + ' x' + str(item[1]) + '\n'
        self.priceRenderer = Text(costStr, 25, [imageBtn.pos[0], imageBtn.pos[1] + imageBtn.size[1] - 40])
        self.rect = pygame.rect.Rect(imageBtn.pos[0], title.position[1],imageBtn.size[0], self.priceRenderer.position[1] + self.priceRenderer.size[1] - title.position[1])
    def click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.selected = not self.selected
            return True
        else:
            return False