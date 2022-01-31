from builtins import set, property

import pygame
import random
import time


def ObjectSysteme():
    global wavesEffect
    global nextSpawn
    if time.time() > nextSpawn:
        objects.append(Object())
        nextSpawn += random.randint(1, 4)

    for obj in objects:
        wavesEffect = (random.randint(0, 3), random.randint(0, 3))
        obj.blit()
        if obj.pos[0] - int(obj.imageSize *1.5) < pygame.mouse.get_pos()[0] < obj.pos[0] + int(obj.imageSize*1.5) and \
                obj.pos[1] - int(obj.imageSize*1.5) < pygame.mouse.get_pos()[1] < obj.pos[1] + int(
                obj.imageSize *1.5) and mousseClick:
            obj.onClick()
            objects.remove(obj)
            del obj

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
    global survivorMax, survivor, survivorSpawnTime
    factors = {
        'watter harvester': 2,
        'fishing': 2,
        'campfire' : 2,
        'dormitory' : 3

    }
    results = {
        'watter harvester': 0,
        'fishing': 0,
        'campfire' : 0,
        'dormitory' : 0
    }

    scale = [32, 32]
    img = {
        'watter harvester': pygame.transform.scale(pygame.image.load('src/watter factor.png'), scale),
        'fishing': pygame.transform.scale(pygame.image.load('src/fish.png'), scale),
        'campfire': pygame.transform.scale(pygame.image.load('src/satisfaction.png'), scale),
        'dormitory': pygame.transform.scale(pygame.image.load('src/more survivor.png'), scale)
    }
    for rft in rafts:
        if rft.building is not None:
            if factors.get(rft.building.name):
                results[rft.building.name] += factors[rft.building.name]


    survivorMax = factors['dormitory']


    if survivorMax > survivor >= 2:
        if time.time() > survivorSpawnTime and results['watter harvester'] - survivor > 0 and results['fishing'] - survivor > 0 and results['campfire'] - survivor > 0:
            survivor += 1
            survivorSpawnTime = time.time() + random.randint(1, 4)

    decalage = 0
    for result in results:
        final = results[result] - survivor
        if final >= 0:
            bliter = font.render(str(final), True,  (0, 255, 0))
        else:
            bliter = font.render(str(final), True,  (255, 0, 0))
        SCREEN.blit(bliter, [20 + decalage, SCREEN_SIZE[1] - 50 ])
        SCREEN.blit(img[result], [20 + decalage + scale[0], SCREEN_SIZE[1] - 50 ])
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

def addNewRaft(rafts):
    if sell('wood', 10):
        rafts.append(raft([pygame.mouse.get_pos()[0] // SIZE, pygame.mouse.get_pos()[1] // SIZE]))
        for rft in rafts:
            rft.reloadImg(rafts)

pygame.init()

font = pygame.font.SysFont("arial", 30)

pygame.display.set_caption('raft')

CLOCK = pygame.time.Clock()

SIZE = 100

SCREEN_SIZE = (1280, 640)

WATTER = pygame.transform.scale(pygame.image.load('src/watter.png'), (SIZE, SIZE))

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
    'campfire': [pygame.transform.scale(pygame.image.load('src/campfire.png'), (SIZE, SIZE)), {'wood' : 4, 'leaf' : 3, 'plastic' : 0}],

}


nextSpawn = time.time() + random.randint(1, 4)
survivorSpawnTime = time.time() + random.randint(1, 4)
objects = []

survivorMax = 2

survivor = 2

rafts = [raft([6 , 3], 'dormitory')]
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

menuCreationBuildings = [menu_upgrade([0,0],'fishing', [-100, -100]), menu_upgrade([0,0],'fishing', [0, -100]), menu_upgrade([0,0],'fishing', [100, -100])]
in_menu = False
mousseClick = False

menuBuilding = menuCreateBuild((SCREEN_SIZE[0] //7 * 6, int(SCREEN_SIZE[1]//6* 0.5)), (SCREEN_SIZE[0] //7, int(SCREEN_SIZE[1]*0.75)), (50,50,50,128))

selected = None


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
                            addNewRaft(rafts)

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

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_LCTRL]:
                if event.key == pygame.K_w:
                    inventory['wood'] += 5
                if event.key == pygame.K_p:
                    inventory['plastic'] += 5
                if event.key == pygame.K_l:
                    inventory['leaf'] += 5

    for x in range((SCREEN_SIZE[0]//SIZE) + 1):
        for y in range((SCREEN_SIZE[1] // SIZE) + 1):
            SCREEN.blit(WATTER, (x * SIZE, y * SIZE))

    ObjectSysteme()

    for rft in rafts:
        rft.bliter()

    if in_menu:
        for menuCreationBuilding in menuCreationBuildings:
            menuCreationBuilding.blit()

    menuBuilding.blit()
    ressource()
    suvivorSys()
    CLOCK.tick(60)
    pygame.display.update()
    SCREEN.fill((0,0,0))

