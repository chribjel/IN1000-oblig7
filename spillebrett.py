from random import randint
from celle import Celle

class Spillebrett:
    ## makes list which is the basis of the playboard
    #
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner

        self._rutenett = [[Celle() for i in range(self._kolonner)] for i in range(self._rader)]

        self.gen = 0
    
    ## generates the board
    #
    def generer(self):
        for row in self._rutenett:
            for unit in row:
                deadOrAlive = randint(0,2)
                if deadOrAlive < 2:
                    unit.settDoed()
                else:
                    unit.settLevende()
    
    ## outputs playboard
    #
    def tegnBrett(self):
        for _ in range(10):
            print("")
        for row in self._rutenett:
            print("")
            for unit in row:
                print(unit.hentStatusTegn(), end="")
        print("")
    
    ## finds status of each neighbouring cell
    #
    def finnNabo(self, x, y):
        nabo = []
        if x != 0:
            nabo.append(self._rutenett[y][x-1])
            try:
                nabo.append(self._rutenett[y+1][x-1])
            except IndexError:
                pass
            if y != 0:
                nabo.append(self._rutenett[y-1][x-1])

        if y != 0:
            try:
                nabo.append(self._rutenett[y-1][x+1])
            except IndexError:
                pass
            nabo.append(self._rutenett[y-1][x])

        try:
            nabo.append(self._rutenett[y][x+1])
        except IndexError:
            pass
        try:
            nabo.append(self._rutenett[y+1][x+1])
        except IndexError:
            pass
        try:
            nabo.append(self._rutenett[y+1][x])
        except IndexError:
            pass

        return nabo

    ## updates board based on certain rules
    #
    def oppdatering(self):
        bliLevende = []
        bliDoed = []

        for y in range(len(self._rutenett)):
            for x in range(len(self._rutenett[y])):
                unit = self._rutenett[y][x]
                
                naboer = self.finnNabo(x, y)
                liveCount = 0
                for nabo in naboer:
                    if nabo.erLevende():
                        liveCount += 1
                
                if unit.erLevende():
                    if liveCount < 2:
                        bliDoed.append(unit)
                    elif liveCount > 3:
                        bliDoed.append(unit)
                if not unit.erLevende():
                    if liveCount == 3:
                        bliLevende.append(unit)
        
        for unit in bliLevende:
            unit.settLevende()
        for unit in bliDoed:
            unit.settDoed()
        
        self.gen += 1

    ## returns amount of alive cells
    #
    def finnAntallLevende(self):
        liveCount = 0
        for row in self._rutenett:
            for unit in row:
                if unit.erLevende():
                    liveCount += 1
        return liveCount