from builtins import set, property

import pygame
import random
import time

class Object:
    def __init__(self):
        self.name = random.choice(list(inventory.keys()))

        self.quantity = random.randint(1, 5)
        self.pos= [-20, random.randint(0, SCREEN_SIZE[1]) - 400]
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



class menuCreateBuild:
    def __init__(self, pos:tuple, size:tuple, bgColor:list):
        class case:
            def __init__(self, name: str, pos: tuple, size: int):
                self.name = name
                self.pos = pos
                self.size = size

            def blit(self):
                if menuBuilding.selected == self.name:
                    pygame.draw.rect(SCREEN, (00,30,00,200), (self.pos, [self.size-5, self.size-5]))
                SCREEN.blit(
                    pygame.transform.scale(pygame.transform.rotate(RAFT, 45), (self.size, self.size)),
                    self.pos)
                SCREEN.blit(
                    pygame.transform.scale(pygame.transform.rotate(bats[self.name][0], 45), (self.size, self.size)),
                    self.pos)

            def onClick(self):
                if  menuBuilding.selected == self.name:
                    menuBuilding.selected = ''
                    return
                menuBuilding.selected = self.name

        self.selected = ''
        self.pos = pos
        self.size = size
        self.bgColor = bgColor
        sizeCase = self.size[1] // len(bats)
        self.cases = []
        for bat in bats:
            self.cases.append(case(bat, pos, sizeCase))
            pos = (pos[0], pos[1] + sizeCase )

    def __repr__(self):
        return 'pos : ' + str(self.pos) + ' size : ' + str(self.size) + ' Color : ' + str(self.bgColor)


    def blit(self):
        pygame.draw.rect(SCREEN, self.bgColor, (self.pos, self.size))
        for thiscase in self.cases:
            thiscase.blit()

    def onCLick(self, moussePos):
        for thiscase in self.cases:
            if thiscase.pos[0] < moussePos[0] < thiscase.pos[0] + thiscase.size and thiscase.pos[1] < moussePos[1] < thiscase.pos[1] + thiscase.size:
                thiscase.onClick()



class menu_upgrade:
    def __init__(self, pos:tuple, batiment:str , decalage:tuple):
        self.posWithoutDecalage = pos
        self.batiment = batiment
        self.decalage = decalage
        self.pos = [self.posWithoutDecalage[0] + self.decalage[0], self.posWithoutDecalage[1] + self.decalage[1]]

    def __repr__(self):
        return 'pos raft : '+ str(self.pos)+ ' build : '+ str(self.batiment)

    def onClick(self):
        for mat  in bats[self.batiment][1]:
            quantity = bats[self.batiment][1][mat]
            print(mat, quantity)
            if not sell(mat, quantity):
                return


        if self.batiment in batimentSelected.menu:
            global in_menu
            in_menu = False
            batimentSelected.building = batimentSelected.batiment(self.batiment)
            batimentSelected.menu.remove(self.batiment)

    def blit(self):
        self.pos = [self.posWithoutDecalage[0] + self.decalage[0], self.posWithoutDecalage[1] + self.decalage[1]]
        SCREEN.blit(pygame.transform.scale(PORTHOLE, [int(SIZE*0.75), int(SIZE*0.75)]), self.pos)
        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(RAFT,(SIZE//2, SIZE//2)), 45), self.pos)

        if bats.get(self.batiment):
            build = bats[self.batiment][0]
        else :
            build = bats['mapping'][0]
        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(build,(SIZE//2, SIZE//2)), 45), self.pos)



class raft:
    def __init__(self, pos:tuple):
        self.pos = pos
        self.building = None
        self.menu = ['fishing', 'watter harvester', 'dormitory']

    def __repr__(self):
        result = 'position : '+ str(self.pos)
        if self.building is not None:
            result += 'build : '+ str(self.building)
        return result

    class batiment:
        def __init__(self, name: str):
            self.name = name

        def __repr__(self):
            return 'name : '+ str(self.name)

        def blit(self, pos):
            if bats.get(self.name):
                SCREEN.blit(bats[self.name][0], [pos[0] * SIZE, pos[1] * SIZE])
            else:
                SCREEN.blit(bats['mapping'][0], [pos[0] * SIZE, pos[1] * SIZE])

    def bliter(self):
        SCREEN.blit(RAFT, [self.pos[0] * SIZE, self.pos[1] * SIZE])
        if self.building is not None:
            self.building.blit(self.pos)

    def buy(self, build):
        for mat in bats[build][1]:
            quantity = bats[build][1][mat]
            if not sell(mat, quantity):
                return
        self.building = self.batiment(build)
        print(self.building)

    def onClick(self):
        if self.building is None:
            if  menuBuilding.selected != '':
                menuCreationBuildings[id].batiment = self.menu[id]
        else:
            global in_menu
            in_menu = True
            for id in range(len(self.menu)):
                menuCreationBuildings[id].posWithoutDecalage = [self.pos[0] * SIZE, self.pos[1] * SIZE]
                menuCreationBuildings[id].batiment = self.menu[id]

def spawnObject():
    global nextSpawn
    if time.time() > nextSpawn:
        objects.append(Object())
        nextSpawn += random.randint(1, 4)

def sell(name, price):
    if inventory[name] >= price:
        inventory[name] -= price
        return True
    return False

def WhatOnPosition(pos):
    temp_raft = None
    for rft in rafts:
        if pos == rft.pos:
            temp_raft = rft

    return temp_raft

def ressource():
    x_pos = 20
    y_pos  = 20

    survivorText = font.render(str(survivor), True, (0, 0, 0))
    SCREEN.blit(survivorText, [SCREEN_SIZE[0] - (survivorText.get_width() + 20), y_pos])

    dict = {
        'wood' : WOOD,
        'leaf' : LEAF,
        'plastic' : PLASTIC
    }
    for name, image in dict.items():
        SCREEN.blit(image, (x_pos, y_pos))
        SCREEN.blit(font.render(str(inventory[name]), True , (255, 255, 255)), (x_pos + 40 , y_pos))
        y_pos += 40

def suvivorSys():
    global survivorMax, survivor
    factors = {
        'watter harvester': 2,
        'fishing': 2
    }
    results = {
        'watter harvester': 0,
        'fishing': 0
    }

    scale = [32, 32]
    img = {
        'watter harvester': pygame.transform.scale(pygame.image.load('src/watter factor.png'), scale),
        'fishing': pygame.transform.scale(pygame.image.load('src/fish.png'), scale)
    }
    max_personne = 0
    for rft in rafts:
        if rft.building is not None:
            if factors.get(rft.building.name):
                results[rft.building.name] +=1
            if factors.get('dortory'):
                max_personne += 1


    survivorMax = max_personne

    decalage = 0
    for result in results:
        final = results[result] * factors[result] - survivor
        if final >= 0:
            bliter = font.render(str(final), True,  (0, 255, 0))
        else:
            bliter = font.render(str(final), True,  (255, 0, 0))
        SCREEN.blit(bliter, [20 + decalage, SCREEN_SIZE[1] - 50 ])
        SCREEN.blit(img[result], [20 + decalage+  scale[0], SCREEN_SIZE[1] - 50 ])
        decalage += bliter.get_width() + 64
    if survivorMax < survivor:
        survivor = survivorMax
    survivor = max(survivor, 1)

def whatAround(pos_map):
    changers = [-1, 1]
    result = []

    for changer in changers:
        result.append(WhatOnPosition([pos_map[0] + changer, pos_map[1]]))
        result.append(WhatOnPosition([pos_map[0], pos_map[1] + changer]))

    return result


pygame.init()

font = pygame.font.SysFont("arial", 30)

pygame.display.set_caption('raft')

CLOCK = pygame.time.Clock()

SIZE = 100

SCREEN_SIZE = (1280, 640)

WATTER = pygame.transform.scale(pygame.image.load('src/watter.png'), (SIZE, SIZE))

RAFT = pygame.transform.scale(pygame.image.load('src/raft.png'), (SIZE, SIZE))

inventory = {
    'wood' : 99,
    'leaf' : 99,
    'plastic' : 99
}

WOOD = pygame.transform.scale(pygame.image.load('src/wood.png'), (30, 30))
LEAF = pygame.transform.scale(pygame.image.load('src/branchage.png'), (30, 30))
PLASTIC = pygame.transform.scale(pygame.image.load('src/plastic.png'), (30, 30))

PORTHOLE = pygame.transform.scale(pygame.image.load('src/menu-bulle.png'), (SIZE, SIZE))

bats = {
    'fishing' : [pygame.transform.scale(pygame.image.load('src/fishing.png'), (SIZE, SIZE)), {'wood' : 3, 'leaf' : 2, 'plastic' : 2}],
    'mapping': [pygame.transform.scale(pygame.image.load('src/mapping.png'), (SIZE, SIZE)), {'wood' : 5, 'leaf' : 0, 'plastic' : 2}],
    'watter harvester': [pygame.transform.scale(pygame.image.load('src/watter harvester.png'), (SIZE, SIZE)), {'wood' : 2, 'leaf' : 2, 'plastic' : 5}],
    'dormitory': [pygame.transform.scale(pygame.image.load('src/dormitory.png'), (SIZE, SIZE)), {'wood' : 0, 'leaf' : 4, 'plastic' : 2}],
    'campfire': [pygame.transform.scale(pygame.image.load('src/mapping.png'), (SIZE, SIZE)), {'wood' : 4, 'leaf' : 3, 'plastic' : 0}],

}


nextSpawn = time.time() + random.randint(1, 4)
objects = []

survivorMax = 1

survivor = 1

rafts = []
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

menuCreationBuildings = [menu_upgrade([0,0],'fishing', [-100, -100]), menu_upgrade([0,0],'fishing', [0, -100]), menu_upgrade([0,0],'fishing', [100, -100])]
in_menu = False
mousseClick = False

menuBuilding = menuCreateBuild((SCREEN_SIZE[0] //7 * 6, int(SCREEN_SIZE[1]//6* 0.5)), (SCREEN_SIZE[0] //7, int(SCREEN_SIZE[1]*0.75)), (50,50,50,128))

selected = None

rafts.append(raft([6 , 3]))

while True:

    if mousseClick:
        mousseClick = False
        menuBuilding.onCLick(pygame.mouse.get_pos())
        if menuBuilding.selected == '':
            if in_menu:
                for menuCreationBuilding in menuCreationBuildings:
                    if menuCreationBuilding.pos[0] < pygame.mouse.get_pos()[0] < menuCreationBuilding.pos[0] + SIZE and menuCreationBuilding.pos[1] < pygame.mouse.get_pos()[1] < menuCreationBuilding.pos[1] + SIZE:
                        menuCreationBuilding.onClick()

                        break
                    in_menu = False
            else:
                mousse_map = [pygame.mouse.get_pos()[0] //SIZE , pygame.mouse.get_pos()[1] // SIZE]
                batimentSelected = WhatOnPosition([pygame.mouse.get_pos()[0] //SIZE , pygame.mouse.get_pos()[1] // SIZE])
                if batimentSelected == None :
                    arounds = whatAround(mousse_map)
                    for around in arounds:
                        if isinstance(around, raft):
                            if sell('wood' , 10):
                                rafts.append(raft([pygame.mouse.get_pos()[0] //SIZE , pygame.mouse.get_pos()[1] // SIZE]))
                else:
                    batimentSelected.onClick()
        else:
            in_menu = False
            batimentSelected = WhatOnPosition([pygame.mouse.get_pos()[0] // SIZE, pygame.mouse.get_pos()[1] // SIZE])
            if not batimentSelected == None:
                batimentSelected.buy(menuBuilding.selected)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousseClick = True
        else: mousseClick = False

    for x in range((SCREEN_SIZE[0]//SIZE) + 1):
        for y in range((SCREEN_SIZE[1] // SIZE) + 1):
            SCREEN.blit(WATTER, (x * SIZE, y * SIZE))

    for rft in rafts:
        rft.bliter()

    if in_menu:
        for menuCreationBuilding in menuCreationBuildings:
            menuCreationBuilding.blit()

    spawnObject()
    for obj in objects:
        wavesEffect = (random.randint(0, 3), random.randint(0, 3))
        obj.blit()
        if obj.pos[0] - (obj.imageSize // 2) < pygame.mouse.get_pos()[0] < obj.pos[0] + int(obj.imageSize*1.5) and obj.pos[1] - (obj.imageSize // 2) < pygame.mouse.get_pos()[1] < obj.pos[1] + obj.imageSize + int(obj.imageSize*1.5) and mousseClick:
            obj.onClick()
            objects.remove(obj)
            del obj

    print(inventory)

    menuBuilding.blit()
    ressource()
    suvivorSys()
    CLOCK.tick(60)
    pygame.display.update()
    SCREEN.fill((0,0,0))

