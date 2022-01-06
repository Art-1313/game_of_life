import numpy as np
import organism

class Field:

    def __init__(self, size, start_field):
        self.__map = np.ndarray(shape=(size), dtype=int)
        self.__map_created = np.ndarray(shape=(size), dtype=int)
        self.__map_dead = np.ndarray(shape=(size), dtype=int)
        for i in range(size[0]):
            for j in range(size[1]):
                self.__map[i][j] = start_field[i][j]
                self.__map_created[i][j] = start_field[i][j]
                self.__map_dead[i][j] = start_field[i][j]
        self.__organisms = set()
        self.__organisms_dead = set()
        self.__organisms_created = set()
        for i in range(size[0]):
            for j in range(size[1]):
                if (self.__map[i][j]):
                    o = organism.Organism((i, j), self)
                    self.__organisms.add(o)

    def Action(self):
        for i in self.__organisms:
            i.Move()
        self.__map = self.__map_dead + self.__map_created - self.__map
        self.__ReMap()
        self.__ReSet()

    def AddOrganism(self, o):
        self.__map_created[o.Position()] = 1
        self.__organisms_created.add(o)

    def DeleteOrganism(self, o):
        self.__map_dead[o.Position()] = 0
        self.__organisms_dead.add(o)

    def Neighbours(self, pos):
        neighbours = 0
        for i in range(3):
            for j in range(3):
                neighbours += self.__map[((i - 1) + pos[0]) % self.Size()[0]][((j - 1) + pos[1]) % self.Size()[1]]
        return neighbours - self.__map[pos[0] % self.Size()[0]][pos[1] % self.Size()[1]]
    
    def Occupied(self, pos):
        return self.__map_created[pos[0] % self.Size()[0]][pos[1] % self.Size()[1]]

    def Size(self):
        return self.__map.shape

    def __ReMap(self):
        for i in range(self.__map.shape[0]):
            for j in range(self.__map.shape[1]):
                self.__map_created[i][j] = self.__map[i][j]
                self.__map_dead[i][j] = self.__map[i][j]

    def __ReSet(self):
        self.__organisms = self.__organisms_created.union(self.__organisms.difference(self.__organisms_dead))
        self.__organisms_dead = set()
        self.__organisms_created = set()
