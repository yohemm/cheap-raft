import pygame

class Raft:
    def __init__(self, pos:tuple, building = None):
        self.pos = pos
        self.building = None
        if building is not None:
            self.building = self.batiment(building)
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

        def blit(self, pos, bats, screen, size):
            if bats.get(self.name):
                screen.blit(bats[self.name][0], [pos[0] * size, pos[1] * size])
            else:
                screen.blit(bats['mapping'][0], [pos[0] * size, pos[1] * size])

    def bliter(self, image , screen, size):
        screen.blit(image, [self.pos[0] * size, self.pos[1] * size])
        if self.building is not None:
            self.building.blit(self.pos,, screen, size)

    def buy(self, build, bats):
        for mat in bats[build][1]:
            quantity = bats[build][1][mat]
            if not sell(mat, quantity):
                return
        self.building = self.batiment(build)
        print(self.building)

    def onClick(self, menuBuilding, menuCreationBuildings):
        if self.building is None:
            if menuBuilding.selected != '':
                menuCreationBuildings[id].batiment = self.menu[id]
        else:
            global in_menu
            in_menu = True
            for id in range(len(self.menu)):
                menuCreationBuildings[id].posWithoutDecalage = [self.pos[0] * SIZE, self.pos[1] * SIZE]
                menuCreationBuildings[id].batiment = self.menu[id]
