from basic import *
import raft
import pygame
class Game:
    def __init__(self, screen, unity, level:int = 0, rafts:list = [raft.Raft(build='fishing')], bats:list = [], pnjs:list=[], money:int = 0, inventory:dict = {'wood':0,'plastic':0,'leaf':0}):
        self.SCREEN = screen
        self.UNITY = unity
        self.level = level
        self.rafts = rafts
        self.bats = bats
        self.villagers = []
        self.money = money
        self.cost = {
            'raft': [('wood', 5)],
            'campfire': [('wood', 3), ('leaf', 1)],
            'dormiroty': [('plastic', 2), ('leaf', 2)],
            'watter harvester': [('plastic', 2), ('wood', 2)],
            'fishing': [('wood', 2), ('leaf', 2)],
            'mapping': (['wood', 3], ['leaf', 1],['plastic', 2])
        }
        self.villager = 2
        self.inventory = inventory
        self.menuVillager = Text('')
        self.menuInventory = Text('La Zone en \n personne')
        self.menuBat = Menu([0, self.SCREEN.get_size()[1]//1.5],[self.SCREEN.get_size()[0], self.SCREEN.get_size()[1]//3])
        self.mapMove = [self.SCREEN.get_size()[0]//2 - self.UNITY//2, self.SCREEN.get_size()[0]//2 - self.UNITY//2]
    def reloadStat(self):
        self.villagerStat = {
            'food' : 0,
            'watter' : 0,
            'hummor' : 0
        }
        association = {
            'food' : ('fishing', 1),
            'watter' : ('watter harvester', 1),
            'hummor' : ('campfire', 2),
        }
        for categori in association:
            for raft in self.rafts:
                if not raft.build == None and raft.build.type == association[categori][0]:
                    self.villagerStat[categori] += association[categori][1]

    def blitMap(self, SCREEN, UNITY):
        #rafts
        watterSize = 50
        for y in range(SCREEN.get_size()[1]//watterSize + 1):
            for x in range(SCREEN.get_size()[0]//watterSize + 1):
                SCREEN.blit(pygame.transform.scale(pygame.image.load('src/watter.png'), (watterSize, watterSize)), (x * watterSize, y * watterSize))
        for raft in self.rafts:
            SCREEN.blit(pygame.transform.scale(pygame.image.load('src/raft/simple.png'), (100, 100)), [raft.position[0] * self.UNITY + self.mapMove[0], raft.position[1] + self.UNITY + self.mapMove[1]])
            #bats
            if not raft.build == None:
                SCREEN.blit(raft.build.setImage(), realPos(raft.position, SCREEN, UNITY))


    def buy(self, name:str):

        possibleToBuy = True
        for material in self.cost[name]:
            if not self.inventory[material[0]] >= material[1]:possibleToBuy = False
        if possibleToBuy:
            for material in self.cost[name]:self.inventory[material[0]] -= material[1]
        return possibleToBuy

    def pressed(self):
        mousseMap = moussePosMap(self.SCREEN, self.UNITY)
        RaftOnPos = False
        for singleRaft in self.rafts:
            if singleRaft.position[0] == mousseMap[0] and singleRaft.position[1] == mousseMap[1]:
                RaftOnPos = True
                if not singleRaft.build == None: print('Menu Upgrade')
                else: print('Menu create')
                break
        if not RaftOnPos and not whatAround(mousseMap, self.rafts) == []:
            if self.buy('raft'):
                self.rafts.append(raft.Raft(mousseMap))

    def blitEntity(self, entity):
        self.SCREEN.blit(entity.image, entity.position)

    def blitMenu(self):
        pygame.draw.rect(self.SCREEN, (60,60, 40), [self.menuBat.position, self.menuBat.size])

