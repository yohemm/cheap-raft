import pygame

class MenuCreateBuild:
    def __init__(self, pos:tuple, size:tuple, bgColor:list, bats):
        class case:
            def __init__(self, name: str, pos: tuple, size: int):
                self.name = name
                self.pos = pos
                self.size = size

            def blit(self, screen, menuBuilding):
                if menuBuilding.selected == self.name:
                    pygame.draw.rect(screen, (00,30,00,200), (self.pos, [self.size-5, self.size-5]))
                screen.blit(
                    pygame.transform.scale(pygame.transform.rotate(RAFT, 45), (self.size, self.size)),
                    self.pos)
                screen.blit(
                    pygame.transform.scale(pygame.transform.rotate(bats[self.name][0], 45), (self.size, self.size)),
                    self.pos)

            def onClick(self, menuBuilding):
                if menuBuilding.selected == self.name:
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


    def blit(self, screen):
        pygame.draw.rect(screen, self.bgColor, (self.pos, self.size))
        for thiscase in self.cases:
            thiscase.blit(self)

    def onCLick(self, moussePos):
        for thiscase in self.cases:
            if thiscase.pos[0] < moussePos[0] < thiscase.pos[0] + thiscase.size and thiscase.pos[1] < moussePos[1] < thiscase.pos[1] + thiscase.size:
                thiscase.onClick(self)



class Menu_upgrade:
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
