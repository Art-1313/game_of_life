class Organism:

    def __init__(self, pos, field):
        self.__position = pos
        self.__field = field

    def Move(self):
        self.__Create()
        self.__Die()

    def __Create(self):
        for i in range(3):
            for j in range(3):
                if (not (self.__field.Occupied(
                                                (((i - 1) + self.__position[0]) % self.__field.Size()[0],
                                                ((j - 1) + self.__position[1]) % self.__field.Size()[1]))
                                                ) and
                    (self.__field.Neighbours(
                                                (((i - 1) + self.__position[0]) % self.__field.Size()[0], 
                                                ((j - 1) + self.__position[1]) % self.__field.Size()[1])) == 3)
                                                ):
                    o = Organism((((i - 1) + self.__position[0]) % self.__field.Size()[0], ((j - 1) + self.__position[1]) % self.__field.Size()[1]), self.__field)
                    self.__field.AddOrganism(o)

    def __Die(self):
        if not (2 <= self.__field.Neighbours(self.__position) <= 3):
            self.__field.DeleteOrganism(self)

    def Position(self):
        return self.__position
