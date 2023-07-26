import os, pygame
from CreamyUI.function import *

class dummy:
    def __init__(self, **settings) -> None:
        pass

    def draw(self, **settings) -> None:
        window :pygame.surface.Surface = settings.get("window", None)
        if (not window): return
        pass

class image:
    def __init__(self, **settings) -> None:
        self.pos = settings.get("pos", (0, 0))
        self.size = settings.get("size", (0, 0))
        self.path = settings.get("path", "")

        exist = os.path.isfile(self.path)
        self.image = LoadTexture(self.path) if exist else LoadTexture(".\\CreamyUI\\tex\\fail.png")
        size = self.image.get_size()
        if (self.size != size): self.image = pygame.transform.smoothscale(self.image, self.size)

        pass
    
    def draw(self, **settings) -> None:
        window :pygame.surface.Surface = settings.get("window", None)
        if (not window): return
        
        window.blit(self.image, self.pos)

class text:
    def __init__(self, **settings) -> None:
        self.pos = settings.get("pos", (0, 0))
        self.text = settings.get("text", "")
        self.fontname = settings.get("font", "Arial")
        self.fontsize = settings.get("fontsize", 16)
        self.font = font(self.fontname, self.fontsize)
        self.color = settings.get("color", (0, 0, 0))
        self.align = settings.get("align", "left")
        pass

    def draw(self, **settings) -> None:
        window :pygame.surface.Surface = settings.get("window", None)
        if (not window): return

        DrawText(self.text, self.font, window, self.pos, self.align, self.color)
        pass