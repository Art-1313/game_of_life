import numpy as np
import organism
import os

class Field:

    def __init__(self, size, start_field):
        self.__map = np.ndarray(shape=(size[0], size[1]), dtype=int)
        self.__map_created = np.ndarray(shape=(size[0], size[1]), dtype=int)
        self.__map_dead = np.ndarray(shape=(size[0], size[1]), dtype=int)
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


    def Draw(self):
        os.system('clear')
        print(self.__map)
        for i in self.__organisms:
            i.Move()
        self.__map = self.__map_dead + self.__map_created - self.__map
        self.__Remap()
        self.__organisms = self.__organisms_created.union(self.__organisms.difference(self.__organisms_dead))
        self.__organisms_dead = set()
        self.__organisms_created = set()

    def AddOrganism(self, o):
        self.__map_created[o.Position()] = 1
        self.__organisms_created.add(o)

    def DeleteOrganism(self, o):
        self.__map_dead[o.Position()] = 0
        self.__organisms_dead.add(o)

    def Neighbours(self, pos):
        neigbours = self.__map[(pos[0] - 1):(pos[0] + 2), (pos[1] - 1):(pos[1] + 2)]
        return neigbours.sum() - self.__map[pos]
    
    def Occupied(self, pos):
        return self.__map_created[pos]

    def __Remap(self):
        for i in range(self.__map.shape[0]):
            for j in range(self.__map.shape[1]):
                self.__map_created[i][j] = self.__map[i][j]
                self.__map_dead[i][j] = self.__map[i][j]