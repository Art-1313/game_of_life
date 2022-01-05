import time

class Render:

    def __init__(self, field, iteration):
        self.__field = field
        self.__iteration = iteration

    def Play(self):
        for i in range(self.__iteration):
            self.__field.Draw()
            time.sleep(0.1)

    def __Show(self):
        pass