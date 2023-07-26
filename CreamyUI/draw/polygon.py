import pygame, copy
from CreamyUI.draw.draw import *

class polygon:
    def __init__(self, cordinates:tuple|list, color:tuple,
                 stroke:int=1, strokecolor:tuple=(255, 255, 255)
                 ) -> None:
        # =======================================
        
        self.CordsCount = len(cordinates)
        self.cordinates = cordinates
        self.color = color
        self.stroke = stroke
        self.strokecolor = strokecolor

        # =======================================

        self.x_sorted = copy.deepcopy(cordinates)
        self.y_sorted = copy.deepcopy(cordinates)
        self.x_sorted.sort(key=lambda x:x[0])
        self.y_sorted.sort(key=lambda y:y[1])
        
        self.MinX, self.MaxX = self.x_sorted[0][0], self.x_sorted[-1][0]
        self.MinY, self.MaxY = self.y_sorted[0][1], self.y_sorted[-1][1]
        self.size = (self.MaxX-self.MinX, self.MaxY-self.MinY)

        self.surface = pygame.surface.Surface(self.size, pygame.SRCALPHA).convert_alpha()

        for i in range(self.CordsCount):
            i = self.CordsCount-i-1

            curr = cordinates[i]
            next = cordinates[i-1]

            aaline(self.surface, strokecolor, (curr[0]-self.MinX, curr[1]-self.MinY), (next[0]-self.MinX, next[1]-self.MinY), stroke)

        # =======================================

        pass

    def draw(self, window:pygame.surface.Surface) -> None:
        window.blit(self.surface, (self.MinX, self.MinY))