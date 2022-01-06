import time
import pygame as pg
import numpy as np

class Render:

    def __init__(self, field, fps):
        self.__field = field
        pg.init()
        pg.display.set_caption("LIFE")
        self.__screen = pg.display.set_mode((field.Size()[1] * 10, field.Size()[0] * 10))
        self.__clock = pg.time.Clock()
        self.__fps = fps
        self.__run = True

    def Play(self):
        while self.__run:
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                        self.__run = False
            self.__Show()
            self.__clock.tick(self.__fps)
        pg.quit()

    def __Show(self):
        surf = pg.Surface(self.__screen.get_size())
        for i in range(self.__field.Size()[0]):
            for j in range(self.__field.Size()[1]):
                cl = tuple(np.array([255, 255, 255]) * self.__field.Occupied([i, j]))
                rect = pg.Rect(j * self.__screen.get_height() / self.__field.Size()[0], i * self.__screen.get_width() / self.__field.Size()[1],
                                self.__screen.get_height() / self.__field.Size()[0], self.__screen.get_width() / self.__field.Size()[1])
                pg.draw.rect(surf, cl, rect)
                pg.draw.rect(surf, (255, 0, 0), rect, width=1)
        self.__screen.fill((0, 0, 0))
        self.__screen.blit(surf, (0, 0))
        pg.display.flip()
        self.__field.Action()