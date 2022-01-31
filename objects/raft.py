
import pygame

class raft:
    def __init__(self, pos:tuple, building = None):
        self.pos = pos
        self.building = None
        if building is not None:
            self.building = self.batiment(building)
        self.menu = ['fishing', 'watter harvester', 'dormitory']
        self.image = pygame.transform.scale(pygame.image.load('src/raft/simple.png'), (SIZE, SIZE))

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
    def reloadImg(self, rafts):
        horizontal = 'simple'
        vertical = 'simple'
        for raft in rafts:
            if raft.pos[1] == self.pos[1]:
                if raft.pos[0] == self.pos[0] - 1:
                    vertical = 'right'
                if raft.pos[0] == self.pos[0] + 1:
                    if vertical == 'right':
                        vertical = 'center'
                        print(vertical + '-' + horizontal + '.png')
                    else:
                        vertical = 'left'
            if raft.pos[0] == self.pos[0]:
                if raft.pos[1] == self.pos[1] - 1:
                    horizontal = 'down'
                if raft.pos[1] == self.pos[1] + 1:
                    if horizontal == 'down':
                        print(vertical + '-' + horizontal + '.png' + str( self.pos))
                        horizontal = 'middle'
                    else:
                        horizontal = 'up'
        if vertical == 'simple' and horizontal == 'simple':
            self.image = pygame.transform.scale(pygame.image.load('src/raft/simple.png'), (SIZE, SIZE))
        elif vertical == 'simple' and not horizontal == 'simple':
            self.image = pygame.transform.scale(pygame.image.load('src/raft/'+horizontal+'.png'), (SIZE, SIZE))
        elif not vertical == 'simple' and horizontal == 'simple':
            self.image = pygame.transform.scale(pygame.image.load('src/raft/'+vertical+'.png'), (SIZE, SIZE))
        else:
            self.image = pygame.transform.scale(pygame.image.load('src/raft/' + vertical +'-' +horizontal + '.png'), (SIZE, SIZE))

    def bliter(self):
        SCREEN.blit(self.image, [self.pos[0] * SIZE, self.pos[1] * SIZE])
        if self.building is not None:
            self.building.blit(self.pos)

    def buy(self, build):
        for mat in bats[build][1]:
            quantity = bats[build][1][mat]
            if not sell(mat, quantity):
                return
        self.building = self.batiment(build)

    def onClick(self):
        if self.building is None:
            if menuBuilding.selected != '':
                menuCreationBuildings[id].batiment = self.menu[id]
        else:
            global in_menu
            in_menu = True
            for id in range(len(self.menu)):
                menuCreationBuildings[id].posWithoutDecalage = [self.pos[0] * SIZE, self.pos[1] * SIZE]
                menuCreationBuildings[id].batiment = self.menu[id]
